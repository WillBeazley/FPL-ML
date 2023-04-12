import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
import double_gameweek as double


def predictions_linear(pos):
    directory = f"data\\ML_prediction_{pos}.csv"

    df = pd.read_csv(directory)
    df = df.iloc[:,[1,2,3,4,5,6,7]]

    return df.nlargest(len(df), "total_points")

def predictions_random(pos):
    directory = f"data\\ML_prediction_{pos}_random_forest.csv"

    df = pd.read_csv(directory)
    df = df.iloc[:,[1,2,3,4,5,6,7]]

    return df.nlargest(len(df), "total_points")

def predictions_svm(pos):
    directory = f"data\\ML_prediction_{pos}_SVM.csv"

    df = pd.read_csv(directory)
    df = df.iloc[:,[1,2,3,4,5,6,7]]

    return df.nlargest(len(df), "total_points")

def GUI():

    headings = ["  first Name  ", "  Last Name  ", " Players Team ", "Upcoming opponent", " Player Value ", "  Gameweek  ", " Predicted Points "]

    layout_1 = [[sg.Text("Prediction Window")], [sg.Button("GK"), sg.Button("DEF"), sg.Button("MID"), sg.Button("FWD")], 
                [sg.Slider(range=(3.5, 13.5), default_value=8.5, resolution=.1, expand_x=True, enable_events=True, orientation='horizontal', 
                key='PRICE')], [sg.Table(values=[], headings=headings, auto_size_columns=True, key='OUTPUT')]]

    window = sg.Window("Best Players", layout_1, size=(1200, 380))

    while(True):
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "GK":
            print(values["PRICE"])
            players = (predictions_random("GK"))
            players = double.double_gw(players)
            gk_df = players[players["value"] <= float(values["PRICE"])*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
            price = gk_df.to_string(index=False)
            data = gk_df[0:].values.tolist()
            window["OUTPUT"].update(values=data)
            print(gk_df)
        elif event == "DEF":
            print(values["PRICE"])
            players = (predictions_random("DEF"))
            players = double.double_gw(players)
            def_df = players[players["value"] <= float(values["PRICE"])*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
            price = def_df.to_string(index=False)
            data = def_df[0:].values.tolist()
            window["OUTPUT"].update(values=data)
            print(def_df)
        elif event == "MID":
            print(values["PRICE"])
            players = (predictions_random("MID"))
            players = double.double_gw(players)
            mid_df = players[players["value"] <= float(values["PRICE"])*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
            price = mid_df.to_string(index=False)
            data = mid_df[0:].values.tolist()
            window["OUTPUT"].update(values=data)
            print(mid_df)
        elif event == "FWD":
            print(values["PRICE"])
            players = (predictions_random("FWD"))
            players = double.double_gw(players)
            fwd_df = players[players["value"] <= float(values["PRICE"])*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
            price = fwd_df.to_string(index=False)
            data = fwd_df[0:].values.tolist()
            window["OUTPUT"].update(values=data)
            print(fwd_df)
        
    window.close()

GUI()




"""
    print("\nBEST PLAYERS FOR EACH POSITION:\n")
    print("enter 'exit' at anypoint to close the program\n")
    position = input("Please select which position you would like - 1.GK 2.DEF 3.MID 4.FWD: ")
    value = input("\nplease select a budget for your player: ")

    if position == "GK" or position == "1":
        players = (predictions_random("GK"))
        print()
        gk_df = players[players["value"] <= float(value)*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4]]
        print(gk_df.to_string(index=False))
    elif position == "DEF" or position == "2":
        players = (predictions_random("DEF"))
        print()
        def_df = players[players["value"] <= float(value)*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,3,4],[5,0,1,2,3,4]]
        print(def_df.to_string(index=False))
    elif position == "MID" or position == "3":
        players = (predictions_random("MID"))
        print()
        mid_df = players[players["value"] <= float(value)*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,3,4],[5,0,1,2,3,4]]
        print(mid_df.to_string(index=False))
    elif position == "FWD" or position == "4":
        players = (predictions_random("FWD"))
        print()
        fwd_df = players[players["value"] <= float(value)*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,3,4],[5,0,1,2,3,4]]
        print(fwd_df.to_string(index=False))
    elif position == "exit" or value == "exit":
        break
    else:
        print("\n------------------------------------------------------------------------------")
        print("ERROR !! TRY AGAIN")
        print("--------------------------------------------------------------------------------\n")
"""