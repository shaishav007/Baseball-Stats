from django.db import models

# Create your models here.
#so we probably will have 4 models - Team , Player, Hitterstats, Pitcherstats
class TeamRecord(models.Model):
    teamid = models.IntegerField()
    name = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    logo = models.CharField(max_length=50) #contains the url of the 
    abbreviation = models.CharField(max_length=10)
    wins = models.IntegerField()
    losses = models.IntegerField()
    pct = models.DecimalField(max_digits=6,decimal_places=3)
    gb = models.CharField(max_length=10)
    l10 = models.CharField(max_length=3)
    diff = models.IntegerField()

    def packageIt(self):
        # returns a dictionary which can probably pass off as a json
        package = {
            "id":self.teamid,
            "name" : self.name,
            "league" : self.league,
            "logo" : self.logo,
            "abbreviation" : self.abbreviation,
            "wins" : self.wins,
            "losses" : self.losses,
            "pct" : self.pct,
            "gb" : self.gb,
            "l10" : self.l10,
            "diff" : self.diff
        }
        return package

class Player(models.Model):
    teamId = models.IntegerField()
    playerId = models.IntegerField()
    name = models.CharField(max_length=50)
    pos = models.CharField(max_length=50)
    jerseyNumber = models.CharField(max_length=4)
    age = models.IntegerField()
    height = models.CharField(max_length=50)
    weight = models.IntegerField()
    drafted = models.IntegerField()
    batside = models.CharField(max_length=1)
    pitchHand = models.CharField(max_length=1)
    
    team = models.CharField(max_length=50)
    games = models.IntegerField() 
    pa = models.IntegerField()
    hits = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    hr = models.IntegerField()
    sb = models.IntegerField()
    so = models.IntegerField()
    bb = models.IntegerField() 
    obp = models.DecimalField(max_digits=4,decimal_places=3)
    ops = models.DecimalField(max_digits=4,decimal_places=3)
    slg = models.DecimalField(max_digits=4,decimal_places=3)
    avg = models.DecimalField(max_digits=4,decimal_places=3)

    ip = models.CharField(max_length=10)
    wins = models.IntegerField()
    losses = models.IntegerField()
    sv = models.IntegerField()
    era = models.DecimalField(max_digits=3,decimal_places=2)
    whip = models.DecimalField(max_digits=3,decimal_places=2)
    h = models.IntegerField()
    r = models.IntegerField()
    so = models.IntegerField()
    bb = models.IntegerField()
    hr9 = models.DecimalField(max_digits=3,decimal_places=2)
    ops = models.DecimalField(max_digits=4,decimal_places=3)
    
    def packageIt(self):
        # returns a dictionary which can probably pass off as a json
        package = {
            "teamId" : self.teamId,
            "playerId" : self.playerId,
            "name" : self.name,
            "pos" : self.pos,
            "jerseyNumber" : self.jerseyNumber,
            "age" : self.age,
            "height" : self.height,
            "weight" : self.weight,
            "drafted" : self.drafted,
            "batside" : self.batside,
            "pitchHand" : self.pitchHand,

            "team":self.team,
            "games":self.games,
            "pa":self.pa,
            "hits":self.hits,
            "doubles":self.doubles,
            "triples":self.triples,
            "hr":self.hr,
            "sb":self.sb,
            "so":self.so,
            "bb":self.bb,
            "obp":self.obp,
            "ops":self.ops,
            "slg":self.slg,
            "avg":self.avg,

            "ip" : self.ip,
            "wins" : self.wins,
            "losses" : self.losses,
            "sv" : self.sv,
            "era" : self.era,
            "whip" : self.whip,
            "h" : self.h,
            "r" : self.r,
            "so" : self.so,
            "bb" : self.bb,
            "hr9" : self.hr9,
            "ops" : self.ops
        
        }
        return package


class HitterStats(models.Model):
    year = models.IntegerField()
    playerId = models.IntegerField()
    team = models.CharField(max_length=50)
    teamId = models.IntegerField()
    games = models.IntegerField() 
    pa = models.IntegerField()
    hits = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    hr = models.IntegerField()
    sb = models.IntegerField()
    so = models.IntegerField()
    bb = models.IntegerField() 
    obp = models.DecimalField(max_digits=4,decimal_places=3)
    ops = models.DecimalField(max_digits=4,decimal_places=3)
    slg = models.DecimalField(max_digits=4,decimal_places=3)
    
    def packageIt(self):
        # returns a dictionary which can probably pass off as a json
        package = {
            "year" : self.year,
            "playerId" : self.playerId,
            "team" : self.team,
            "teamId":self.teamId,
            "games" : self.games,
            "pa" : self.pa,
            "hits" : self.hits,
            "doubles" : self.doubles,
            "triples" : self.triples,
            "hr" : self.hr,
            "sb" : self.sb,
            "so" : self.so,
            "bb" : self.bb,
            "obp" : self.obp,
            "ops" : self.ops,
            "slg" : self.slg
        }
        return package
    


class PitcherStats(models.Model):
    year = models.IntegerField()
    playerId = models.IntegerField()
    team = models.CharField(max_length=50)
    teamId = models.IntegerField()
    games = models.IntegerField()
    ip = models.CharField(max_length=10)
    wins = models.IntegerField()
    losses = models.IntegerField()
    sv = models.IntegerField()
    era = models.DecimalField(max_digits=3,decimal_places=2)
    whip = models.DecimalField(max_digits=3,decimal_places=2)
    h = models.IntegerField()
    r = models.IntegerField()
    so = models.IntegerField()
    bb = models.IntegerField()
    hr9 = models.DecimalField(max_digits=3,decimal_places=2)
    ops = models.DecimalField(max_digits=4,decimal_places=3)

    def packageIt(self):
        # returns a dictionary which can probably pass off as a json
        package = {
            "year" : self.year,
            "playerId" : self.playerId,
            "team":self.team,
            "teamId":self.teamId,
            "games" : self.games,
            "ip" : self.ip,
            "wins" : self.wins,
            "losses" : self.losses,
            "sv" : self.sv,
            "era" : self.era,
            "whip" : self.whip,
            "h" : self.h,
            "r" : self.r,
            "so" : self.so,
            "bb" : self.bb,
            "hr9" : self.hr9,
            "ops" : self.ops
        }
        return package
    