# Premier League Betting Strategies

## Introduction:
This project sets out to investigate the returns on using different type of strategies for Premier League games in each season:

Category 1:

•	Betting on Home Team to Win

•	Betting on Away Team to Win

•	Betting on a Draw

•	Betting on Underdog to Win

•	Betting on Favourite to Win

Category 2:

•	Betting on a specific team to win


The motives for this project were to see if there’s any advantage to have a bet strategy set out before the start of each season, rather than on a game-to-game basis, which is more common. 

I retrieved datasets from https://www.football-data.co.uk . These datasets contained statistics of every match of the season. The statistics we focused on were: Home Team, Away Team, Full Time Result, Pre-Match Home odds (Bet365), , Pre-Match Draw odds (Bet365), , Pre-Match Away odds (Bet365). Bet365 are one of the most popular bookies worldwide, so this gives an accurate representation of the odds. 

I chose the 10 seasons from 2012/13 to 2021/22.  The way I conducted this experiment was to imagine having placed a $1 bet on each game for each season based on the categories aforementioned. This sums up to a $380 investment each season for Category 1 and a $38 investment each season for Category 2

# Category 1 Analysis:

<img width="450" alt="Screenshot 2023-01-31 at 16 51 40" src="https://user-images.githubusercontent.com/122220434/215828822-80ccb010-9f21-4ef8-96ae-4dd6b6951235.png">


After cleaning the data, these are the summary statistics which summarise the returns for each feature in category 1. 
For every single feature, on average, you would make a loss each season (negative return).  

The maximum return ($108.76) was from a season betting on Away wins, and the minimum return was a season betting on Draws (-98.49$). 
If I was to guess from personal domain knowledge, I would say that this maximum return for away wins came in either the 2020/21 or the 2021/22 season when there were no crowds in stadiums, which largely reduces the home advantage in football matches. It is possible that the bookies didn't account for this to a large enough extent.


<img width="423" alt="Screenshot 2023-01-31 at 16 52 02" src="https://user-images.githubusercontent.com/122220434/215828896-a5a376ce-abd5-44c3-9427-f65b9973c8ab.png">


This heatmap shows the correlation between returns for each of the categories. It mainly gives us a better idea of which combinations perform better and worse together

Home and away having a negative correlation is a trivial finding, as if home wins is positive, this almost definitely implies there were far less away wins than home wins, thus a negative return.

Home and Favourite have a positive correlation (0.46) which could suggest a positive relationship between them. This is likely due to the fact that home teams are most likely to be favourites. This means that if home return is positive, favourite return is likely to be positive too.

Similarly, Away and Underdog have a strong positive correlation of 0.84. Again away teams are most often the underdogs. This means that if away return is positive, underdog return is likely to be positive too.


<img width="473" alt="Screenshot 2023-01-31 at 16 52 27" src="https://user-images.githubusercontent.com/122220434/215828998-2ee20cb9-a0b2-4f95-ab6b-87388cf94dec.png">


This is an overall line plot of the data. It can be seen for each feature, there is heavy variance in returns from season-to-season. Most of the returns were negative, depicted by the return mainly being below the black (break-even) line.


<img width="455" alt="Screenshot 2023-01-31 at 16 53 09" src="https://user-images.githubusercontent.com/122220434/215829170-e6c5a176-fdc7-475e-b907-b017d41ce400.png">


Isolating the line plot for away, we can see that the spike in returns for betting on away wins was indeed in 2020/21, as previously suggested, where there was no crowds in football stadiums. 


<img width="456" alt="Screenshot 2023-01-31 at 16 53 24" src="https://user-images.githubusercontent.com/122220434/215829230-0a25d156-0ec4-42a8-8505-c1beeb901341.png">


One of the biggest observations that can be seen in draw, is that it is in almost a perfect zig-zag like motion, with the return increasing in one year and falling again the next year (albeit not necessarily being positive) (exception = 2015/16 season where it continued to increase).


<img width="463" alt="Screenshot 2023-01-31 at 16 53 42" src="https://user-images.githubusercontent.com/122220434/215829309-5b673b14-58f3-4eee-9707-9efb5ff5c3e3.png">


Interestingly, returns for betting on underdog wins were very positive in the 2020/21 season (just like away wins were), before falling greatly in 2021/22, which suggests the bookies corrected their pricing model for underdogs the next season. Either this or there were far fewer underdog wins in 2021/22 than there was in 2020/21. On further inspection, there were 100 underdog wins in the 2020/21 season, and 71 in the 2021/22 season, which suggests the latter.


## Category 2 Analysis:

Category 2 consists of betting on a specific team to win each game. Since the Premier League consists of a relegation system, I made a list of the 9 teams that haven’t been relegated since the 2012/13 season to analyse fairly. 
These teams are:
•	Chelsea

•	Man City

•	Man United

•	Tottenham

•	Everton

•	Liverpool

•	West Ham

•	Arsenal

•	Southampton


<img width="460" alt="Screenshot 2023-01-31 at 16 54 10" src="https://user-images.githubusercontent.com/122220434/215829429-aa5af462-7940-4704-bcfb-937c9cd1564f.png">


Note that the investment for the teams is $38 in each season. From these statistics, both Tottenham and West Ham have a positive mean return. Including the features in category 1, these are the only positive means throughout this experiment.

The minimum return was Southampton (-22.54 dollars), which is perhaps expected as they are a less established club than the others so on average they would win far less games throughout a season than the others.

West Ham had the highest return (35.23 dollars). This is a lot higher than any of the other club's maximums (next highest is Southampton at 15.5 dollars) so this could be considered an outlier in the dataset. This is an incredible return on investment of 92.71% for that season.

For the two positive means, This means that over the 10 seasons, Tottenham and West Ham, they had an average return on investment of 9.06% and 7.24% respectively. 

These are quite high in my opinion. The huge maximum return discussed above skews the mean West Ham value though so caution must be taken on that regard.


<img width="460" alt="Screenshot 2023-01-31 at 16 54 27" src="https://user-images.githubusercontent.com/122220434/215829484-34f5cddc-e944-4a11-8c6c-0b9e70f35406.png">


This plot is obviously quite hard to interpret for each individual team, but we can see the large volatility in the returns from season to season, making it difficult to make out any type of pattern. The outlier of the large return by West Ham in the 2015/16 season is a big standout, as well as the low return of Southampton in the 2017/18 season. Overall it is clear that a loss is the most common return, or else a very low positive return.


<img width="463" alt="Screenshot 2023-01-31 at 16 54 52" src="https://user-images.githubusercontent.com/122220434/215829571-99b2df66-3e95-49c2-9ccd-e4b1305ed2e9.png">


Isolating the West Ham statistics, it can be seen their returns hover between low positive and low negative returns, and that one outlier season with a very large positive return is skewing their data so the mean is positive.


<img width="462" alt="Screenshot 2023-01-31 at 16 55 07" src="https://user-images.githubusercontent.com/122220434/215829628-fdb4a3dc-66c6-4ee9-87a9-257f3fd415b9.png">


Interestingly, over the 10 years, returns for Tottenham were negative for only 2 of them. This can be put down to the over-performance of this football club from ~ 2012-2018 in my opinion. Very few critics, and evidently the bookies, expected Tottenham to perform as well as they did throughout these seasons. Thus, if you were someone who had predicted Tottenham’s fortunes beforehand, a healthy profit could’ve been made from placing bets on them to win each game.  


# Conclusion:

Before carrying out this experiment, I was considering attempting to try and predict future returns on the features in the categories, but upon analysing the data, the lack of patterns and huge variance in the returns have led me to refrain from doing so.

The key to consistently profitable betting is an edge on the bookies, which is naturally very difficult due to their highly skilled teams and comprehensive use of data. This project makes it pretty clear to me that a strategy of consistently betting on an specific outcome throughout a season does not yield a positive return. 

Returns from year to year seem to follow a “random-walk” . Football is a difficult game to predict, and simply setting out to use one of these strategies aforementioned will not (or at least will rarely) lead to consistent positive returns. It will take a lot more than these pre-defined methods to beat the bookies!

