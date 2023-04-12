import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

important_stats = {}

directory = "C:\\Users\\William\\Documents\\Cardiff University\\Year 3\\One Semester Project\\Code\\data\\current\\players"

def plot_graph(directory, list):

    FPL_names = os.listdir(directory)
    print(list)

    x = np.array([])
    y = np.array([])

    for name in FPL_names:
        df = pd.read_csv(f"data\current\players\{name}\gw.csv", usecols=list)
        # Experiment with different x
        x = np.append(x, df._get_value(0, list[1]))
        # Total points = y
        y = np.append(y, df._get_value(0, 'total_points'))


    # Plot x againsts y (total points)
    plt.scatter(x, y)
    plt.xlabel(list[1:])
    plt.ylabel("total points")
    plt.show()
    

plot_graph(directory, ["total_points", "was_home"])
