import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def import_training(pos):
    directory = f"data\\all_seasons_{pos}.csv"

    df = pd.read_csv(directory)

    return df

def points_per_game(df):

    ## get average points for each player ##

    players = {}

    player_count = {}

    final_column = []

    # 9 = "total_points"
    # 2 = "name"

    for i in range(0, len(df)):
        if df.iloc[i, 9] != 0:
            if df.iloc[i, 2] in player_count:
                final_column.append(players[df.iloc[i, 2]] / player_count[df.iloc[i, 2]])
                player_count[df.iloc[i, 2]] = player_count[df.iloc[i, 2]] + 1
                players[df.iloc[i, 2]] = (df.iloc[i, 9] + players[df.iloc[i, 2]])
            else:
                final_column.append(0)
                player_count[df.iloc[i, 2]] = 1
                players[df.iloc[i, 2]] = df.iloc[i, 9]
        else:
            if df.iloc[i, 2] in players:
                final_column.append(players[df.iloc[i, 2]] / player_count[df.iloc[i, 2]])
            else:
                final_column.append(0)

    df["points_per_game"] = final_column

    return df

def goals_conceded(df):

    ## get all goals conceded ##

    final_column = []

    final_column_minutes = []

    players = {}

    player_minutes = {}

    # 19 = "goals_conceded"
    # 2 = "name"
    
    for j in range(0, len(df)):
        if df.iloc[j, 2] not in players:
            final_column.append(0)
            final_column_minutes.append(0)
            players[df.iloc[j, 2]] = df.iloc[j, 19]
            player_minutes[df.iloc[j, 2]] = df.iloc[j, 20]
        elif df.iloc[j, 2] in players:
            if player_minutes[df.iloc[j, 2]] == 0 and players[df.iloc[j, 2]] == 0:
                final_column.append(0)
                final_column_minutes.append(player_minutes[df.iloc[j, 2]])
            else:
                final_column.append(players[df.iloc[j, 2]] / (player_minutes[df.iloc[j, 2]] / 90))
                final_column_minutes.append(player_minutes[df.iloc[j, 2]] + df.iloc[j, 19])
                player_minutes[df.iloc[j, 2]] = (player_minutes[df.iloc[j, 2]] + df.iloc[j, 20])
                players[df.iloc[j, 2]] = (players[df.iloc[j, 2]] + df.iloc[j, 19])
                print(df.iloc[j, 2])

    df["goals_conceded_per_game"] = final_column
    df["total_minutes"] = final_column_minutes

    #print(df)

    return df


def norm_training(df, pos):

    df.replace(np.nan, 0)

    dataframes = []
    dataframes_years = []

    years = ["2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22"]

    for year in years:

        df_season = df[df["season_x"] == year]

        df_season = df_season.sort_values("GW")

        df_season = goals_conceded(df_season)

        df_season = points_per_game(df_season)

        max = df_season["GW"].max()

        for i in range(1, max+1):
            df1 = df_season[df_season["GW"] == i]
            df1 = df1.copy()
            df1["ict_index"] = df1["ict_index"] / df1["ict_index"].abs().max()
            df1["creativity"] = df1["creativity"] / df1["creativity"].abs().max()
            df1["influence"] = df1["influence"] / df1["influence"].abs().max()
            df1["threat"] = df1["threat"] / df1["threat"].abs().max()
            dataframes.append(df1)

        merge_df = reduce(lambda left, right: pd.merge(left, right, how="outer"),dataframes)

        dataframes_years.append(merge_df)

    final_df = reduce(lambda left, right: pd.merge(left, right, how="outer"),dataframes_years)

    final_df = final_df.loc[:,["season_x", "name", "position", "fixture", "ict_index", "opponent_team", "opp_team_name", "selected", "total_points", "value", "was_home", "GW", "creativity", "influence", "threat", "transfers_in", "transfers_out", "goals_conceded", "minutes", "goals_conceded_per_game", "points_per_game", "total_minutes"]]

    final_df.to_csv(rf"data\\all_seasons_{pos}_normalized.csv", encoding='utf-8-sig')

    return final_df

GK = import_training("GK")
DEF = import_training("DEF")
MID = import_training("MID")
FWD = import_training("FWD")

norm_training(GK, "GK")
norm_training(DEF, "DEF")
norm_training(MID, "MID")
norm_training(FWD, "FWD")




