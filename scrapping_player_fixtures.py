import requests
import json
import time
import pandas as pd

def get_fixture_data(x):
    
    ## Highest id is 745
    full_url = (f"https://fantasy.premierleague.com/api/element-summary/{x}/")

    response = requests.get(f"https://fantasy.premierleague.com/api/element-summary/{x}/")

    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))

    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(1)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def get_player_data():

    response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))

    responseStr = response.text
    data = json.loads(responseStr)

    return data

def scrape(gameweek):
    data = {"player_id": [],
            "name": [],
            "position": [],
            "player_team_name": [],
            "ict_index": [],
            "opponent_team": [],
            "opp_team_name": [],
            "value": [],
            "was_home": [],
            "GW": [],
            "creativity": [],
            "influence": [],
            "threat": [],
            "transfers_in": [],
            "transfers_out": [],
            "chance_of_playing": [],
            "form": [],
            "goals_conceded": [],
            "minutes": [],
            "goals_conceded_per_game": [],
            "points_per_game": [],
            "total_minutes": [],
            "first_name": []
            }

    export_df_FWD = pd.DataFrame(data)
    export_df_MID = pd.DataFrame(data)
    export_df_DEF = pd.DataFrame(data)
    export_df_GK = pd.DataFrame(data)

    player = get_player_data()
    teams = get_player_data()["teams"]
    team_names = {}
    team_position = {}

    for i in range(0, len(teams)):
        team_names[i+1] = teams[i]["name"]
        team_position[team_names[i+1]] = teams[i]["position"]

    #print(team_names)
    #print(teams)

    for i in range(0, len(player["elements"]) - 1):
        
        player_id = player["elements"][i]["id"]
        fixture = get_fixture_data(player_id)

        ###             CHANGE GAMEWEEK IN IF STATEMENT FOR PLAYERS PLAYING IN THAT GAMEWEEK            ###
        if player["elements"][i]["chance_of_playing_next_round"] != 0 and player["elements"][i]["chance_of_playing_next_round"] != 25 and fixture["fixtures"][0]["event"] == gameweek:
            name = player["elements"][i]["web_name"]
            position = player["elements"][i]["element_type"]
            value = player["elements"][i]["now_cost"]
            influence = float(player["elements"][i]["influence"])
            creativity = float(player["elements"][i]["creativity"])
            threat = float(player["elements"][i]["threat"])
            ict_index = float(player["elements"][i]["ict_index"])
            next_round = player["elements"][i]["chance_of_playing_next_round"]
            form = player["elements"][i]["form"]
            transfers_in = player["elements"][i]["transfers_in"]
            transfers_out = player["elements"][i]["transfers_out"]
            chance_of_playing = player["elements"][i]["chance_of_playing_next_round"]
            GW = fixture["fixtures"][0]["event"]
            was_home = fixture["fixtures"][0]["is_home"]
            if was_home == True:
                opponent_team = fixture["fixtures"][0]["team_h"]
                opp_team_name = team_names[fixture["fixtures"][0]["team_a"]]
            else:
                opponent_team = fixture["fixtures"][0]["team_a"]
                opp_team_name = team_names[fixture["fixtures"][0]["team_h"]]
            player_team_name = team_names[opponent_team]
            goals_conceded = player["elements"][i]["goals_conceded"]
            minutes = player["elements"][i]["minutes"]
            if minutes != 0:
                goals_conceded_per_game = goals_conceded / (minutes / 90)
            else:
                goals_conceded_per_game = 0
            points_per_game = player["elements"][i]["points_per_game"]
            total_minutes = minutes = player["elements"][i]["minutes"]
            first_name = player["elements"][i]["first_name"]
            #table_position = team_position[opponent_team]

            list_row = [player_id, name, position, player_team_name, ict_index, opponent_team, opp_team_name, value, was_home, GW, creativity, influence, threat, transfers_in, transfers_out, chance_of_playing, form, goals_conceded, minutes, goals_conceded_per_game, points_per_game, total_minutes, first_name]

            if position == 4:
                export_df_FWD.loc[len(export_df_FWD)] = list_row
            if position == 3:
                export_df_MID.loc[len(export_df_MID)] = list_row
            if position == 2:
                export_df_DEF.loc[len(export_df_DEF)] = list_row
            if position == 1:
                export_df_GK.loc[len(export_df_GK)] = list_row

            #print(name)


    export_df_GK = export_df_GK.copy()
    export_df_GK["ict_index"] = export_df_GK["ict_index"] / export_df_GK["ict_index"].abs().max()
    export_df_GK["creativity"] = export_df_GK["creativity"] / export_df_GK["creativity"].abs().max()
    export_df_GK["influence"] = export_df_GK["influence"] / export_df_GK["influence"].abs().max()
    export_df_GK["threat"] = export_df_GK["threat"] / export_df_GK["threat"].abs().max()

    export_df_MID = export_df_MID.copy()
    export_df_MID["ict_index"] = export_df_MID["ict_index"] / export_df_MID["ict_index"].abs().max()
    export_df_MID["creativity"] = export_df_MID["creativity"] / export_df_MID["creativity"].abs().max()
    export_df_MID["influence"] = export_df_MID["influence"] / export_df_MID["influence"].abs().max()
    export_df_MID["threat"] = export_df_MID["threat"] / export_df_MID["threat"].abs().max()

    export_df_DEF = export_df_DEF.copy()
    export_df_DEF["ict_index"] = export_df_DEF["ict_index"] / export_df_DEF["ict_index"].abs().max()
    export_df_DEF["creativity"] = export_df_DEF["creativity"] / export_df_DEF["creativity"].abs().max()
    export_df_DEF["influence"] = export_df_DEF["influence"] / export_df_DEF["influence"].abs().max()
    export_df_DEF["threat"] = export_df_DEF["threat"] / export_df_DEF["threat"].abs().max()

    export_df_FWD = export_df_FWD.copy()
    export_df_FWD["ict_index"] = export_df_FWD["ict_index"] / export_df_FWD["ict_index"].abs().max()
    export_df_FWD["creativity"] = export_df_FWD["creativity"] / export_df_FWD["creativity"].abs().max()
    export_df_FWD["influence"] = export_df_FWD["influence"] / export_df_FWD["influence"].abs().max()
    export_df_FWD["threat"] = export_df_FWD["threat"] / export_df_FWD["threat"].abs().max()

    export_df_FWD.to_csv(r"data\\testing_data_FWD.csv", encoding='utf-8-sig')
    export_df_MID.to_csv(r"data\\testing_data_MID.csv", encoding='utf-8-sig')
    export_df_DEF.to_csv(r"data\\testing_data_DEF.csv", encoding='utf-8-sig')
    export_df_GK.to_csv(r"data\\testing_data_GK.csv", encoding='utf-8-sig')