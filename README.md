# Running the code:

Run automation.py then run best_upcoming_players.py


## Files:

all_seasons.py - extracts data from any data file required

Attribute_correlations.py - creates graphs to show correlation between attributes and total points

automation - runs scrapping_player_fixtures.py functions to extract upcoming gameweek data, Random_forest_all_seasons.py and Linear_regression_all_seasons.py to create
the point predictions which is output to a csv file

best_upcoming_players.py - extracts the predicted points from ML_prediction_{position}_random_forest.csv and outputs them using a GUI

linear_regression_accuracy.py - outputs the accuracy values for the linear regression model

Linear_regression_all_seasons.py - runs the linear regression model on the old and new data and outputs predictions to ML_prediction_{position}.csv

normalize_ict.py - normalizes the ict index, threat, creativity and influence attributes for the old and new data as well as create points per game, goals conceded
and total minutes for all the training data

Random_forest_accuracy.py - outputs the accuracy values for the random forest model

Random_forest_all_seasons.py - runs the random forest model on the old and new data and outputs predictions to ML_prediction_{position}_random_forest.csv

scrapping_player_fixtures.py - scrapes upcoming fixture data from the fantasy premier league api

SVM_all_seasons.py - runs the SVM model on the old and new data and outputs predictions to ML_prediction_{position}_SVM.csv

requirements.txt - all the python libraries necessary to run all the scripts




DATA:

cleaned_merged_seasons.csv = every player from every position with every attribute that has been tracked from 2016

all_seasons_{position}_normalized.csv = training data with normalized ict index, threat, creativity and influence

all_seasons_{position}.csv = traning data that isnt normalized

testing_data_{position}.csv = data used for predicting points. contains upcoming gameweek data for each position

ML_prediction_{position}.csv = linear regression predictions

ML_prediction_{position}_random_forest.csv = random forest predictions
