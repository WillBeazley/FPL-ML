import pandas as pd
import numpy as np

def extract_df():

    directory = "data\\all_seasons_FWD.csv"

    df = pd.read_csv(directory)

    return df

def extract_df_dir(directory):

    df = pd.read_csv(directory)

    return df

def extract_upcoming_df(pos):

    directory = f"data\\testing_data_{pos}.csv"

    df = pd.read_csv(directory)

    return df

def all_columns_df():

    directory = "data\\cleaned_merged_seasons_FWD.csv"

    df = pd.read_csv(directory)

    return df

