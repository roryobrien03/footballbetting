from datasetup import *


def count():
    homecount = 0
    awaycount = 0
    drawcount = 0
    for i in range(len(df)):
        if df2.loc[i, 'home_team_goal_count'] > df2.loc[i, 'away_team_goal_count']:
            homecount += 1
        elif  df2.loc[i, 'home_team_goal_count'] < df2.loc[i, 'away_team_goal_count']:
            awaycount += 1 
        else:
            drawcount += 1
    return print(f"Home count is {homecount}"), print(f"Away count is {awaycount}"), print(f"Draw count is {drawcount}") 

count()                