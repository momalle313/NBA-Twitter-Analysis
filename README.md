# NBA-Twitter-Analysis
Social Sensing and Cyber Physical Systems Project

The source code has four main functionalities:
1) To collect tweets, run the data scraper:
"python scraper.py [team-name]"
For example: "python scraper.py Bulls"
This will append to a file named [team-name]-data.txt
It uses [team-name]-keywords.txt to select tweets that contain the keywords for that team.

The collected data was cleaned by running the command ":%s/\r/ /g" in vim to remove characters that interfered with ASCII encoding. This created a file named [team-name]-data-clean.txt that was used for analysis.

2) To manually classify tweets into a dictionary to use as the training set for sentiment analysis:
"python make-dictionary.py [team-name]"
For example: "python make-dictionary Bulls"
This will append to a file named train-[team-name].csv

3) To calculate the average sentiment of tweets for a certain game:
"python analysis-final.py [team-name] [game-number]"
For example: "python analysis-final.py Bulls 0"
This will output to the command line the results of the sentiment analysis.

4) To run the logistic regression and ROC curve:
Use R or RStudio to run the code in the file R_Analysis.R
It will use the data stored in Social_Sensing_NBA_Data.csv

Team names include:
Bulls
Heat
Rockets

Game numbers range from:
0-7 for Bulls
0-5 for Heat
0-8 for Rockets

