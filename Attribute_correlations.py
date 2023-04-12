import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import all_seasons as wb
import irrelevant_files.Creating_player_form as fo
import all_seasons as ex
import seaborn as sns

df = ex.extract_df_dir("data\\all_seasons_DEF_normalized.csv")

print(df)

def ict_index(label, comp):
    sns.scatterplot(x = df["ict_index"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("Ict index")
    plt.ylabel(comp)
    plt.show()

def opponent_team(label, comp):
    sns.scatterplot(x = df["opponent_team"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("Opponent team")
    plt.ylabel(comp)
    plt.show()

def value(label, comp):
    sns.scatterplot(x = df["value"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("Value")
    plt.ylabel(comp)
    plt.show()

def creativity(label, comp):
    sns.scatterplot(x = df["creativity"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("Creativity")
    plt.ylabel(comp)
    plt.show()

def influence(label, comp):
    sns.scatterplot(x = df["influence"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("Influence")
    plt.ylabel(comp)
    plt.show()

def transfers_in(label, comp):
    sns.scatterplot(x = df["transfers_in"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("Transfers_in")
    plt.ylabel(comp)
    plt.show()

def transfers_out(label, comp):
    sns.scatterplot(x = df["transfers_out"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("Transfers_out")
    plt.ylabel(comp)
    plt.show()

def fixture(label, comp):
    sns.scatterplot(x = df["fixture"], y = df[comp], alpha = 0.5)
    plt.title(label)
    plt.xlabel("fixture")
    plt.ylabel(comp)
    plt.show()

label = "DEF DATASET"

def run_all(label, comp):
    ict_index(label, comp)
    opponent_team(label, comp)
    value(label, comp)
    creativity(label, comp)
    influence(label, comp)
    transfers_in(label, comp)
    transfers_out(label, comp)
    fixture(label, comp)

run_all(label, "total_points")

