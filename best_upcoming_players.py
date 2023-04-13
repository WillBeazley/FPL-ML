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


def tk_window():
    window = tk.Tk()
    window.title("Best Players")
    window.geometry("1200x380")
    window.resizable(False, False)
    #make the window bigger and equal to the size of the screen
    window.state("zoomed")

    #create 4 buttons for each position
    window.gk_button = tk.Button(window, text="GK")    
    window.def_button = tk.Button(window, text="DEF")
    window.mid_button = tk.Button(window, text="MID")
    window.fwd_button = tk.Button(window, text="FWD")

    #place the buttons on the window
    #place the buttons closer to the top of the window
    window.gk_button.grid(row=1, column=0, pady=5, sticky="n")
    window.def_button.grid(row=1, column=1, pady=5, sticky="n")
    window.mid_button.grid(row=1, column=2, pady=5, sticky="n")
    window.fwd_button.grid(row=1, column=3, pady=5, sticky="n")
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
    #move the slider closer to the top of the window
    window.slider = tk.Scale(window, from_=3.5, to=14, orient="horizontal", length=1000, resolution=0.1)
    window.slider.grid(row=2, column=0, columnspan=4, pady=10, sticky="n")
    #make the slider button thicker
    window.slider.config(font=("Arial", 20, "bold"), highlightthickness=0)

    #create a table to display the players 
    #extend the table up closer to the top of the window
    window.table = ttk.Treeview(window, columns=("First Name", "Last Name", "Team", "Opponent", "Value", "Gameweek", "Predicted Points"), show="headings", height=25)
    window.table.grid(row=3, column=0, columnspan=4, pady=10, sticky="n")
    #label the columns of the table
    window.table.heading("First Name", text="First Name")
    window.table.heading("Last Name", text="Last Name")
    window.table.heading("Team", text="Team")
    window.table.heading("Opponent", text="Opponent")
    window.table.heading("Value", text="Value")
    window.table.heading("Gameweek", text="Gameweek")
    window.table.heading("Predicted Points", text="Predicted Points")



    def gk_clicked():
        players = (predictions_random("GK"))
        players = double.double_gw(players)
        #retrieve the price from the slider
        price = window.slider.get()
        gk_df = players[players["value"] <= price*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
        #update the table with the players
        data = gk_df[0:].values.tolist()
        window.table.delete(*window.table.get_children())
        for i in data:
            window.table.insert("", "end", values=i)
        print(gk_df)

    def def_clicked():
        players = (predictions_random("DEF"))
        players = double.double_gw(players)
        price = window.slider.get()
        def_df = players[players["value"] <= price*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
        data = def_df[0:].values.tolist()
        window.table.delete(*window.table.get_children())
        for i in data:
            window.table.insert("", "end", values=i)
        print(def_df)

    def mid_clicked():
        players = (predictions_random("MID"))
        players = double.double_gw(players)
        price = window.slider.get()
        mid_df = players[players["value"] <= price*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
        data = mid_df[0:].values.tolist()
        window.table.delete(*window.table.get_children())
        for i in data:
            window.table.insert("", "end", values=i)
        print(mid_df)

    def fwd_clicked():
        players = (predictions_random("FWD"))
        players = double.double_gw(players)
        price = window.slider.get()
        fwd_df = players[players["value"] <= price*10].sort_values(by="total_points", ascending=False).iloc[[0,1,2,4,5],[5,0,1,2,3,4,6]]
        data = fwd_df[0:].values.tolist()
        window.table.delete(*window.table.get_children())
        for i in data:
            window.table.insert("", "end", values=i)
        print(fwd_df)


    #move the table, slider and buttons to the middle of the window
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)

    #make the buttons bigger and rounder and add a border
    window.gk_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"), command=gk_clicked)
    window.def_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"), command=def_clicked)
    window.mid_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"), command=mid_clicked)
    window.fwd_button.config(height=2, width=10, relief="groove", borderwidth=5, bg="black", fg="white", font=("Arial", 20, "bold"), command=fwd_clicked)

    #open the window
    window.mainloop()

tk_window()