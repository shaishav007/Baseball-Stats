from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from bs4 import BeautifulSoup
from django.db import models
from .models import TeamRecord, Player, HitterStats, PitcherStats
from .utilities import utils

# Create your views here.
def displayOverview(request):
    #general used case to generate dictionaries 
    league_dict,team_dict = utils.getLeagueDict()

    context={}
    
    #alright so the team model can be built by all the data in here.
    league_data_request = requests.get('https://statsapi.mlb.com/api/v1/standings?leagueId=103,104').json()
    league_records=[]
    #so we make an empty team, assign a league division
    
    for entry in league_data_request['records']:
        # entry is each division
        for record in entry['teamRecords']:
            #record is each team's individual record in entry
            currentTeamRecord = TeamRecord(
                teamid = record['team']['id'],
                name = record['team']['name'],
                #league name from dictionary and id provided by the id in division attribute of entry
                league = league_dict[entry['division']['id']],
                logo = 'https://www.mlbstatic.com/team-logos/'+str(record['team']['id'])+'.svg',
                abbreviation = team_dict[record['team']['name']],
                wins = record['leagueRecord']['wins'],
                losses = record['leagueRecord']['losses'],
                pct = record['leagueRecord']['pct'],
                gb = record['gamesBack'],
                l10 = '5-5',
                diff = record['runDifferential']
            )
            #now that the team is ready we can just push it to the teams array
            league_records.append(currentTeamRecord)
    
    #this one is going to have the packaged json data for the team
    leaguePackage={}
    
    #the function below adds the data to this package as a key
    for id,division in league_dict.items():
        #for each division just make sure the teams for the particular league fit in 
        league_teams = []
        for team in league_records:
            if team.league==division:
                #package the team info into the package, this package can now be used in the 
                league_teams.append(team.packageIt())

        leaguePackage[division] = league_teams
    
    #news data from xml
    stories= utils.getStoriesFromUrl('https://www.mlb.com/feeds/news/rss.xml')

    #setting up the context to render
    context={
        'leagues': leaguePackage, #line 46
        'posts':stories   #line 58
    }
    return render(request,'index.html',context)



def loadTeamView(request,teamId):   
    context={}
    # Eventually we will just put them in the database. but that's after the models are finalised
    hitters=[]     #hitters
    pitchers=[]    #pitchers        
    playerInfoUrl = "https://statsapi.mlb.com/api/v1/teams/"+str(teamId)+"/roster/Active?hydrate=person(stats(type=season))"
 
    league_dict,team_dict = utils.getLeagueDict()

    #each team has a subheading with some stats that we can get from here
    teamStanding = 0
    wins = 0
    losses = 0
    gb=""
    division=201
    standings_url = "https://statsapi.mlb.com/api/v1/standings?leagueId=103,104"
    standings_request = requests.get(standings_url).json()
    for record in standings_request['records']:
        for teamRecord in record['teamRecords']:
            if teamId == teamRecord['team']['id']:
                #found the team, index+1 will be the standing
                teamStanding = record['teamRecords'].index(teamRecord)+1
                wins = teamRecord['leagueRecord']['wins']
                losses = teamRecord['leagueRecord']['losses']
                gb=teamRecord['divisionGamesBack']
                division = record['division']['id']


    #2 modes - hitters and pitchers, we can know which one based on the url
    modeUrl = request.META['PATH_INFO']
    mode=modeUrl.split('/')[-2] #this value gives you either hitters or pitchers
    
    
    # we make the hitters and pitchers dictionaries in the same loop, they are in the "roster" array just populating using the Player class defined in models
    players_info = requests.get(playerInfoUrl).json()
    for player in players_info["roster"]:
        if player["position"]["abbreviation"]!='P':
            #if the guy is not a pitcher, we gotta make sure there are hitter stats
            split = player['person']['stats'][0]['splits'][0]['stat'] if 'stats' in player['person'].keys() else "NA"
            currentPlayer = Player(
            teamId = player['parentTeamId'],
            playerId = player["person"]["id"],
            name = player["person"]["fullName"],
            pos = player["position"]["abbreviation"],
            jerseyNumber = player["jerseyNumber"],
            age = player["person"]["currentAge"],
            height = player["person"]["height"],
            weight = player["person"]["weight"],
            drafted = player["person"]["draftYear"] if "draftYear" in player["person"] else "NA",
            batside = player["person"]["batSide"]["code"],
            pitchHand = player["person"]["pitchHand"]["code"],
            games = split['gamesPlayed'] if 'stats' in player['person'].keys() else "NA",
            pa = split["plateAppearances"] if 'stats' in player['person'].keys() else "NA",
            hits = split["hits"] if 'stats' in player['person'].keys() else "NA",
            doubles = split["doubles"] if 'stats' in player['person'].keys() else "NA",
            triples = split["triples"] if 'stats' in player['person'].keys() else "NA",
            hr = split["homeRuns"] if 'stats' in player['person'].keys() else "NA",
            sb = split["stolenBases"] if 'stats' in player['person'].keys() else "NA",
            so = split["strikeOuts"] if 'stats' in player['person'].keys() else "NA",
            bb = split["baseOnBalls"] if 'stats' in player['person'].keys() else "NA",
            obp = split["obp"] if 'stats' in player['person'].keys() else "NA",
            ops = split["ops"] if 'stats' in player['person'].keys() else "NA",
            slg = split["slg"] if 'stats' in player['person'].keys() else "NA",
            avg = split['avg'] if 'stats' in player['person'].keys() else "NA"
            )
            hitters.append(currentPlayer.packageIt())
        else:
            #this means player is a pitcher
            split = player['person']['stats'][0]['splits'][0]['stat'] if 'stats' in player['person'].keys() else "NA"
            currentPlayer = Player(
            teamId = player['parentTeamId'],
            playerId = player["person"]["id"],
            name = player["person"]["fullName"],
            pos = player["position"]["abbreviation"],
            jerseyNumber = player["jerseyNumber"],
            age = player["person"]["currentAge"],
            pitchHand = player["person"]["pitchHand"]["code"],
            ip = split['inningsPitched'] if 'stats' in player['person'].keys() else "NA",
            wins = split['wins'] if 'stats' in player['person'].keys() else "NA",
            losses = split['losses'] if 'stats' in player['person'].keys() else "NA",
            sv = split['saves'] if 'stats' in player['person'].keys() else "NA",
            era = split['era'] if 'stats' in player['person'].keys() else "NA",
            whip = split['whip'] if 'stats' in player['person'].keys() else "NA",
            h = split['holds'] if 'stats' in player['person'].keys() else "NA",
            r = split['runs'] if 'stats' in player['person'].keys() else "NA",
            so = split['strikeOuts'] if 'stats' in player['person'].keys() else "NA",
            bb = split['baseOnBalls'] if 'stats' in player['person'].keys() else "NA",
            hr9 = split['homeRunsPer9'] if 'stats' in player['person'].keys() else "NA",
            ops = split['ops'] if 'stats' in player['person'].keys() else "NA"
            )

            pitchers.append(currentPlayer.packageIt())


    context['subStats']={
        "standing":str(teamStanding)+" in "+league_dict[division],
        "wl":str(wins)+"-"+str(losses),
        "gb":gb
    }

    #get the name of the team from the teamId coz the context will need it
    teamInfoUrl = 'https://statsapi.mlb.com//api/v1/teams/'+str(teamId)
    teamInfo = requests.get(teamInfoUrl).json()
    
    #add it to the context
    context['team'] = teamInfo['teams'][0]['name']
    context['teamId']=teamId
    context['mode'] = mode #line 102
    context['hitters']=hitters #line 107
    context['pitchers']=pitchers #line 107
     
    return render(request,'team.html',context)

def YearlyStatsView(request,teamId,playerId):
    yearlyStatsUrl = "https://statsapi.mlb.com/api/v1/people/"+str(playerId)+"?hydrate=stats(group=[hitting,pitching,fielding],type=[yearByYear])"

    #this is the data we get from the request
    stats_info = requests.get(yearlyStatsUrl).json()

    context={} #data we pass to the template 
    context['player']= stats_info['people'][0]['fullName']
    context['playerId']= stats_info['people'][0]['id']
    
    context['currentTeamId']=teamId
    teamRequest = requests.get('https://statsapi.mlb.com/api/v1/teams/'+str(teamId)).json()
    context['currentTeam'] = teamRequest['teams'][0]['name']

    #gives B/T, Age, height, weight and Drafted year, to be used in the mini table beside the player's pic
    context['miniTableInfo']={
        "bt":str(stats_info['people'][0]['batSide']["code"]+"/"+stats_info['people'][0]['pitchHand']["code"]),
        "age":stats_info['people'][0]['currentAge'],
        "height":stats_info['people'][0]['height'],
        "weight":stats_info['people'][0]['weight'],
        "drafted":stats_info['people'][0]['draftYear'] if 'draftYear' in stats_info['people'][0].keys() else "NA"

    }

    # this stats list is going to have all the info eventually, year by uear stats
    ybyStats=[]
    person = stats_info['people'][0]
    context['Pos'] = person["primaryPosition"]["abbreviation"];
    if person["primaryPosition"]["abbreviation"] != 'P':
        #so the guy is probably a hitter or a fielder so we gotta check his fielding stats maybe?
        if 'stats' in person.keys():
            for stat in person["stats"]:
                #hitting stats are hard to find
                if stat['group']['displayName']=='hitting':
                    for split in stat['splits']:
                        currentStats = HitterStats(
                            year = split['season'],
                            playerId = person['id'],
                            team = split['team']['name'] if 'team' in split.keys() else "NA",
                            teamId = split['team']['id'] if 'team' in split.keys() else "NA",
                            games = split['stat']['gamesPlayed'],
                            pa = split['stat']['plateAppearances'],
                            hits = split['stat']['hits'],
                            doubles = split['stat']['doubles'],
                            triples = split['stat']['triples'],
                            hr = split['stat']['homeRuns'],
                            sb = split['stat']['stolenBases'],
                            so = split['stat']['strikeOuts'],
                            bb = split['stat']['baseOnBalls'],
                            obp = split['stat']['obp'],
                            ops = split['stat']['ops'] ,
                            slg = split['stat']['slg']
                        )

                        ybyStats.append(currentStats.packageIt())

    else:
        #so the guy is a pitcher so we gotta check stats[2] and not stats[0]
        if 'stats' in person.keys():
            for stat in person["stats"]:
                #pitching stats are hard to find
                if stat['group']['displayName']=='pitching':
                    for split in stat['splits']:
                        #this should bring us in the right spot always
                        currentStats = PitcherStats(
                            year = split['season'],
                            playerId = person['id'],
                            team = split['team']['name'] if 'team' in split.keys() else "NA",
                            teamId = split['team']['id'] if 'team' in split.keys() else "NA",
                            games = split['stat']['gamesPlayed'],
                            ip = split['stat']['inningsPitched'],
                            wins = split['stat']['wins'],
                            losses = split['stat']['losses'],
                            sv = split['stat']['saves'],
                            era = split['stat']['era'],
                            whip = split['stat']['era'],
                            h = split['stat']['holds'],
                            r = split['stat']['runs'],
                            so = split['stat']['strikeOuts'],
                            bb = split['stat']['baseOnBalls'],
                            hr9 = split['stat']['hitsPer9Inn'],
                            ops = split['stat']['ops']


                        )
                        ybyStats.append(currentStats.packageIt())

    #finally adding year by year stats to context 
    context['stats']=ybyStats if len(ybyStats)>0 else "stats not available"
    
    return render(request, 'player.html',context)


def setLeaderBoard(request):

    leaderBoardUrl="https://statsapi.mlb.com/api/v1/stats/leaders?leaderCategories=homeRuns"

    leaderBoardResults = requests.get(leaderBoardUrl).json()
    leaders = leaderBoardResults['leagueLeaders'][0]['leaders']

    leaderData=[]
    for leader in leaders:
        entry={
        "rank" : leader['rank'],
        "value" : leader['value'],
        "team" : leader['team']['name'],
        "teamId" : leader['team']['id'],
        "person" : leader['person']['fullName'],
        "personId"  : leader['person']['id'],
        "season" : leader['season']
        }
        leaderData.append(entry)
        

    context={
        "leaders":leaderData
    }
    return render(request,'leaderBoard.html',context)