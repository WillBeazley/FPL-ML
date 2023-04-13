import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
import double_gameweek as double
import tkinter as tk
from tkinter import ttk


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


"""
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

#create a function that creates a tkinter window with a slider and a table
#the slider will be used to select the price of the player
#the table will display the players with the highest predicted points
#the table will be sorted by predicted points
#the table will only display players with a value less than the slider value
#the table will only display the top 5 players
#the table will display the players first name, last name, team, opponent, value, gameweek, predicted points

#the function will take in a position as a parameter
#the function will return the top 5 players for that position

#the function will use the predictions_random function to get the predicted points for each player
#the function will use the double_gw function to get the double gameweek players
#the function will use the slider value to get the players with a value less than the slider value
#the function will use the table to display the players

#the function will use the tkinter library to create the window
#the function will use the tkinter table to display the players

#the function will use the tkinter slider to get the slider value

#the function will use the tkinter button to get the button value

#the function will use the tkinter window to display the window

#the function will use the tkinter window to close the window

#the function will use the tkinter window to get the window value

#the function will use the tkinter window to get the window event

#the function will use the tkinter window to get the window values

#the function will use the tkinter window to get the window event

#the function will use the tkinter library to create the window


def tk_window():
    window = tk.Tk()
    window.title("Best Players")
    window.geometry("1200x380")
    window.resizable(False, False)


    #create 4 buttons for each position
    window.gk_button = tk.Button(window, text="GK")    
    window.def_button = tk.Button(window, text="DEF")
    window.mid_button = tk.Button(window, text="MID")
    window.fwd_button = tk.Button(window, text="FWD")

    #place the buttons on the window
    window.gk_button.grid(row=1, column=0, pady=10)
    window.def_button.grid(row=1, column=1, pady=10)
    window.mid_button.grid(row=1, column=2, pady=10)
    window.fwd_button.grid(row=1, column=3, pady=10)
    #space the buttons out evenly accross the whole window
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)

    #make the buttons change colour when the mouse hovers over them
    window.gk_button.bind("<Enter>", lambda event: window.gk_button.config(bg="white", fg="black"))
    window.gk_button.bind("<Leave>", lambda event: window.gk_button.config(bg="black", fg="white"))
    window.def_button.bind("<Enter>", lambda event: window.def_button.config(bg="white", fg="black"))
    window.def_button.bind("<Leave>", lambda event: window.def_button.config(bg="black", fg="white"))
    window.mid_button.bind("<Enter>", lambda event: window.mid_button.config(bg="white", fg="black"))
    window.mid_button.bind("<Leave>", lambda event: window.mid_button.config(bg="black", fg="white"))
    window.fwd_button.bind("<Enter>", lambda event: window.fwd_button.config(bg="white", fg="black"))
    window.fwd_button.bind("<Leave>", lambda event: window.fwd_button.config(bg="black", fg="white"))
    
    #create a slider to select the price of the player and place it on the window
    window.slider = tk.Scale(window, from_=4.5, to=12, orient="horizontal", length=1000, resolution=0.1)
    window.slider.grid(row=2, column=0, columnspan=4, pady=10)
    #make the slider bigger
    window.slider.config(font=("Arial", 20, "bold"))

    #create a table to display the players 
    window.table = ttk.Treeview(window, columns=("First Name", "Last Name", "Team", "Opponent", "Value", "Gameweek", "Predicted Points"), show="headings")
    window.table.grid(row=3, column=0, columnspan=4, pady=10)
    #label the columns of the table
    window.table.heading("First Name", text="First Name")
    window.table.heading("Last Name", text="Last Name")
    window.table.heading("Team", text="Team")
    window.table.heading("Opponent", text="Opponent")
    window.table.heading("Value", text="Value")
    window.table.heading("Gameweek", text="Gameweek")
    window.table.heading("Predicted Points", text="Predicted Points")
    #if the user clicks on the GK button, display the top 5 goalkeepers
    values = window.slider.get()
    #get gk_button value as a string
    def gk_command():
        print("GK")

    #make the buttons bigger and rounder and add a border
    window.gk_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"), command=gk_command())
    window.def_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"))
    window.mid_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"))
    window.fwd_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"))




    #open the window
    window.mainloop()

tk_window()