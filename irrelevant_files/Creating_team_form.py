import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np



def create_team_form(start, end):

    form = {}

    directory = "C:\\Users\\William\\Documents\\Cardiff University\\Year 3\\One Semester Project\\Code\\data\\current\\team_data.csv"

    df = pd.read_csv(directory, usecols= ["Round Number", "Home Team", "Away Team", "Result"])

    for ind in df.index:
        if df["Home Team"][ind] not in form:
            form[df["Home Team"][ind]] = 0

    df = df[df["Round Number"].between(start, end)]

    print(form)

    for ind in df.index:
        if type(df["Result"][ind]) == str:
            num = df["Round Number"][ind] 
            home = df["Home Team"][ind]
            away = df["Away Team"][ind]
            result =  df["Result"][ind]
            if result[0] > result[4]:
                form[home] += 3
            elif result[0] < result[4]:
                form[away] += 3
            elif result[0] == result[4]:
                form[home] += 1
                form[away] += 1


    temp = sorted(form.items(), key=lambda x:x[1], reverse = True)

    sorted_form = dict(temp)

    return sorted_form

