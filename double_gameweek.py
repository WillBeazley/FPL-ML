import pandas as pd

def double_gw(players):

    dupli = players[players.duplicated(subset=["name", "player_team_name"])]

    if len(dupli) > 0:
        for i in range(len(dupli)):
            for j in range(len(dupli)):
                if dupli.iloc[i, 5] == dupli.iloc[j, 5] and dupli.iloc[i, 0] == dupli.iloc[j, 0]:
                    players.loc[len(players)] = [dupli.iloc[i, 0], dupli.iloc[i, 1], [dupli.iloc[i, 2], dupli.iloc[j, 2]], dupli.iloc[i, 3], dupli.iloc[i, 4], dupli.iloc[i, 5], (dupli.iloc[i, 6] + dupli.iloc[j, 6])]


    return players