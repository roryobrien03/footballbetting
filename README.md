# footballbetting

This project aimed to analyse if it could be profitable to use one consistent strategy for betting in Premier League games throughout a season. I used the 2018/2019 season for this analysis.

There were 5 main categories of strategies I analysed, each adding up to 380 games and hence a $380 stakeL

Betting on the home team to win each game , Betting on the away team to win each game, Betting on a draw in each game, Betting on the underdog (team with lower odds of winning) to win each game, Betting on the favourite (team with higher odds of winning) to win each game

Another category I analysed was if a person was to place a bet on a specific team, for each of their 38 games. This accumulates to a stake of $38


I used python for this project, using pandas to read the csv file downloaded from https://footystats.org , which contained rows and columns of each match and the odds, and then creating functions for the different criteria by iterating through the rows. I made this an interactive experience so anyone could pick the criteria which interested them to see the Return in dollars and Return on Investment (ROI) of the consistent strategies.


Overall, the results of the project were unsurprising. All but one of the consistent strategies resulted in a loss. The only one where a profit was made was betting on the home team to win. This yielded a profit of $20.37 and a Return on Investment of 5.36% . 

What particularly interested me was that the consistent betting on a single team resulted in a loss for all 20 teams. You would almost think that betting on the winners (Man City), who won 32/38 games (84.21% of them) would yield a profit. However it instead results in a $15.89 loss (ROI = -41.82%).


The key to consistently profitable betting is an edge on the bookies, which is naturally very difficult due to their highly skilled teams and comprehensive use of data. This project makes it pretty clear to me that a strategy of consistently betting on an specific outcome does not yield a positive return. Moreover, lots of people use emotion in betting and are more inclined to place bets on the team they support, but the result of this project where there was a loss for each team further shows this isn't a good idea. 

Of course this is a small sample size (only one season), and I would need to repeat this experiment over multiple seasons to provide a conclusive conclusion. I would like to explore if there was a significant change in the returns for betting on home and away games when fans were no longer allowed in the stadium due to COVID-19, as I feel this may be significant. I would also like to create a model to forecast what the expected returns of each of these strategies in future seasons would be. Unfortunately, data for other seasons needs to be paid for on the website I used


