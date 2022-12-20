import requests
import json
from bs4 import BeautifulSoup

def getLeagueDict():
# so for each team in league_request, the .division is going to give out the name of whatever league it was in
    #there are 6 divisions in each team and each division would be populated here.
    league_request = requests.get('https://statsapi.mlb.com/api/v1/teams?sportId=1').json()
    
    #a dictionary that stores league in the structure {...200:'American League West'...}
    leagueDict = {
        team['division']['id']:team['division']['name'] for team in league_request['teams']
    }

    #a dictionary with structure {'Toronto Blue Jays':'TOR','New York Yankees':'NYY'...}
    teamDict ={
        team['name']:team['abbreviation'] for team in league_request['teams']
    }
    return leagueDict,teamDict


#put an rss feed url and get stories back
def getStoriesFromUrl(url):
    stories=[]
    xml_response = requests.get(url)
    soup = BeautifulSoup(xml_response.content,'xml')
    entries = soup.find_all('item')
    for entry in entries:
        story={
            "postTitle" : entry.title.text,
            "postLink" : entry.link.text,
            "postImage" : entry.image['href'],
            "postAuthor" : entry.creator.text,
            "postDate" : entry.pubDate.text[4:16]
        }
        stories.append(story)
    return stories