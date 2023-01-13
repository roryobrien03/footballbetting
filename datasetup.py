import pandas as pd

df = pd.read_csv("pl1819.csv")
df2 = df[['home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count', 'odds_ft_home_team_win', 'odds_ft_draw', 'odds_ft_away_team_win']]