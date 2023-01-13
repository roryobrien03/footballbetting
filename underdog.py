import pandas as pd

df = pd.read_csv("pl1819.csv")

df2 = df[['home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count', 'odds_ft_home_team_win', 'odds_ft_draw', 'odds_ft_away_team_win']]



def hometeamwin():
    win1 = -380
    for i in range(len(df)):
        if df2.loc[i, 'home_team_goal_count'] > df2.loc[i, 'away_team_goal_count']:
            win1 += df2.loc[i, 'odds_ft_home_team_win']
    return print(f"Return = ${win1}"), print(f"ROI = {win1/380}")


def awayteamwin():
    win2 = -380
    for i in range(len(df)):
        if df2.loc[i, 'home_team_goal_count'] < df2.loc[i, 'away_team_goal_count']:
            win2 += df2.loc[i, 'odds_ft_away_team_win']
    return print(f"Return = ${win2}"), print(f"ROI = {win2/380} %")

def draw():
    draw1 = -380
    for i in range(len(df)):
        if df2.loc[i, 'home_team_goal_count'] == df2.loc[i, 'away_team_goal_count']:
            draw1 += df2.loc[i, 'odds_ft_draw']
    return print(f"Return = ${draw1}"), print(f"ROI = {draw1/380} %")

def underdog():
    underdog = -380
    for i in range(len(df)):
        if df2.loc[i, 'odds_ft_home_team_win'] < df2.loc[i, 'odds_ft_away_team_win']:
            if df2.loc[i, 'home_team_goal_count'] > df2.loc[i, 'away_team_goal_count']:
                underdog += df2.loc[i, 'odds_ft_home_team_win']
        elif df2.loc[i, 'odds_ft_home_team_win'] > df2.loc[i, 'odds_ft_away_team_win']:
            if df2.loc[i, 'home_team_goal_count'] < df2.loc[i, 'away_team_goal_count']:
                underdog += df2.loc[i, 'odds_ft_away_team_win']
    return print(f"Return = ${underdog}") , print(f"ROI = {underdog/380} %")

def favourite():
    favourite = -380
    for i in range(len(df)):
        if df2.loc[i, 'odds_ft_home_team_win'] > df2.loc[i, 'odds_ft_away_team_win']:
            if df2.loc[i, 'home_team_goal_count'] > df2.loc[i, 'away_team_goal_count']:
                favourite += df2.loc[i, 'odds_ft_home_team_win']
        elif df2.loc[i, 'odds_ft_home_team_win'] < df2.loc[i, 'odds_ft_away_team_win']:
            if df2.loc[i, 'home_team_goal_count'] < df2.loc[i, 'away_team_goal_count']:
                favourite += df2.loc[i, 'odds_ft_away_team_win']         
    return print(f"Return = ${favourite}") , print(f"ROI = {favourite/380} %")

def welcome():
    global choice
    print("Welcome to my PL 2018/19 season analysis of the amount of money you would get back if you bet $1 on each game, with a consistent criteria of who the bet is on, and hence how much the stake is. For the first 5 categories, this adds up to a total stake of $380 throughout the season. For the specific teams categories, the stake adds up to $38")
    choice = input("Please choose the number linked to the criteria you would like to have the bets placed on. \n 1. Home Team \n 2. Away Team \n 3. Draw \n 4. Underdog \n 5. Favourite \n 6. Specific Team ")
    if choice == "1":
        hometeamwin()
    elif choice == "2":
        awayteamwin()
    elif choice == "3":
        draw()
    elif choice == "4":
        underdog()
    elif choice == "5":
        favourite()
    elif choice == "6":
        teampick()    
    else:
        print("Sorry, this is not an option. Please try again") 
        welcome()

def teampickfunction():
    teamreturn = -38
    for i in range(len(df)):
        if name == df2.loc[i, 'home_team_name']:
            if df2.loc[i, 'home_team_goal_count'] > df2.loc[i, 'away_team_goal_count']:
                teamreturn += df2.loc[i, 'odds_ft_home_team_win']
        elif name == 'away_team_name':
            if df2.loc[i, 'away_team_goal_count'] > df2.loc[i, 'home_team_goal_count']:
                teamreturn += df2.loc[i, 'odds_ft_away_team_win']
    return print(f"Return = ${teamreturn}"), print(f"ROI = {teamreturn/38} %")         


def teampick():
    global name
    choice = input("Please choose the number corresponding to which team you would like to have the bets placed on?")
    if choice == "1":
        name = "Manchester City"
        teampickfunction()
    elif choice == "2":
        name = "Liverpool"
        teampickfunction()
        
    elif choice == "3":
        name = "Chelsea"
        teampickfunction()
       
    elif choice == "4":
        name = "Tottenham Hotspur"
        teampickfunction()

    elif choice == "5":
        name = "Arsenal"
        teampickfunction()

    elif choice == "6":
        name = "Manchester United"
        teampickfunction()

    elif choice == "7":
        name = "Wolverhampton Wanderers"
        teampickfunction()

    elif choice == "8":
        name = "Everton"
        teampickfunction()

    elif choice == "9":  
        name = "Leicester City"
        teampickfunction()

    elif choice == "10":
        name = "West Ham"
        teampickfunction()

    elif choice == "11": 
        name = "Watford" 
        teampickfunction()

    elif choice == "12":
        name = "Crystal Palace"
        teampickfunction()

    elif choice == "13":
        name = "Newcastle United"
        teampickfunction()

    elif choice == "14":
        name = "AFC Bournemouth"
        teampickfunction()

    elif choice == "15":
        name = "Burnley"
        teampickfunction()

    elif choice == "16": 
        name = "Southampton"
        teampickfunction()
     
    elif choice == "17":
        name = "Brighton & Hove Albion"
        teampickfunction()

    elif choice == "18":
        name = "Cardiff City" 
        teampickfunction()

    elif choice == "19":
        name = "Fulham"
        teampickfunction()

    elif choice == "20":
        name = "Huddersfield Town"
        teampickfunction()


    else:
        new = input("Sorry this is not an option. Type 1 to select a team, or 2 to go back to main menu")
        if new == "1":
            teampick()
        elif new == "2":
            welcome()
        else:
            print("Sorry this is not an option. You will be returned to the main menu")
            welcome()        


                                          
welcome()
