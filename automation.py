from Random_forest_all_seasons import position_ML
from Linear_regression_all_seasons import position_ML_lr
from scrapping_player_fixtures import scrape

test = input("What gameweek would you like help with: ")

print("\nPlease wait whilst the program updates. This may take up to 5 minutes")

scrape(int(test))

print("\n65% complete")

position_ML("data\\all_seasons_FWD_normalized.csv", "FWD")
position_ML("data\\all_seasons_MID_normalized.csv", "MID")
position_ML("data\\all_seasons_DEF_normalized.csv", "DEF")
position_ML("data\\all_seasons_GK_normalized.csv", "GK")

print("\n80% complete")

position_ML_lr("data\\all_seasons_FWD_normalized.csv", "FWD")
position_ML_lr("data\\all_seasons_MID_normalized.csv", "MID")
position_ML_lr("data\\all_seasons_DEF_normalized.csv", "DEF")
position_ML_lr("data\\all_seasons_GK_normalized.csv", "GK")

print("\nUpdate is complete\n")
print("Run 'best_upcoming_players.py' to get help with specified gw")