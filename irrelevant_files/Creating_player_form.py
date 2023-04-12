import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


def player_form_dict(gameweek, player_df, bool):

    form = {}

    for z in range(0, len(player_df)):
        if player_df["name"][z] not in form:
            form[player_df["name"][z]] = 0

    if bool == False:
        for j in range(len(player_df)):
            form[player_df["name"][j]] += player_df["total_points"][j]

    for key in form:
        form[key] = form[key] / 4

    return form

def player_form_df(gameweek, player_df):

    bool = False

    if 1 < gameweek < 4:
        player_df = player_df[player_df["GW"].between(0, gameweek - 1)]
    elif gameweek > 3:
        player_df = player_df[player_df["GW"].between(gameweek - 4, gameweek - 1)]
    elif gameweek == 1:
        player_df = player_df[player_df["GW"].between(0, gameweek)]
        bool = True

    player_df = player_df.reset_index(drop=True)

    form = player_form_dict(gameweek, player_df, bool)

    playername = []
    playerpoints = []

    for key in form:
        playername.append(key)
        playerpoints.append(form[key])
    
    player_form_df = pd.DataFrame({"name": playername, "GW": gameweek, "player_form": playerpoints})

    return player_form_df

def create_final_df():
    directory = "data\\merged_gw_2021-22.csv"
    player_df = pd.read_csv(directory, usecols= ["name", "position", "team", "total_points", "opponent_team", "GW", "value", "ict_index", "influence", "was_home", "transfers_in", "transfers_out"])
    player_df["player_form"] = ""

    gameweek_finish = int(player_df.loc[len(player_df)-1, "GW"])

    all_player_form = []

    for i in range(1, gameweek_finish):
        player_form_df_temp = player_form_df(i, player_df)
        all_player_form.append(player_form_df_temp)

    player_form_dataframe = pd.concat(all_player_form)

    final_df = pd.merge(player_df, player_form_dataframe, on=["name", "GW"])
    del final_df["player_form_x"]
    final_df = final_df.rename(columns={"player_form_y": "player_form"})

    return final_df

print(create_final_df().iloc[:,[0,12]])