from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('overview/',views.displayOverview),
    path('overview/team-<int:teamId>/hitters/',views.loadTeamView),
    path('overview/team-<int:teamId>/hitters/player-<int:playerId>/',views.YearlyStatsView),
    path('overview/team-<int:teamId>/pitchers/player-<int:playerId>/',views.YearlyStatsView),
    path('overview/team-<int:teamId>/pitchers/',views.loadTeamView),
    path('overview/team-<int:teamId>/player-<int:playerId>/',views.YearlyStatsView),
    path('overview/team-<int:teamId>/',views.loadTeamView),
    
]