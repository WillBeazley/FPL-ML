from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import all_seasons as wb
import csv

# Predict players points with players positions as parameters
def position_ML_lr(directory, pos):
    df = wb.extract_df_dir(directory)

    new_data = wb.extract_upcoming_df(pos)

    # Create X and Y dataframes
    X = df.iloc[:,[5,6,10,11,12,13,14,15,20,21]]
    Y = df.iloc[:,[9]]

    X_upcoming_data = new_data.iloc[:,[5,6,8,9,10,11,12,13,20,21]]

    X_upcoming_data = X_upcoming_data.replace(np.nan, 0)

    # Replace nan float values with 0 in the X and Y dataframes
    X = X.replace(np.nan, 0)
    Y = Y.replace(np.nan, 0)

    # Split data into 80% test and 20% train
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # Create the model
    model = linear_model.LinearRegression()
    # Apply the training data to the model
    model.fit(X_train, Y_train)

    # Create the predicted total points from the upcoming GW
    Y_pred = model.predict(X_upcoming_data)

    Y_pred_df = pd.DataFrame(Y_pred, columns=["total_points"])

    final_prediction = pd.merge(new_data.iloc[:,[2,4,7,8,10,23]], Y_pred_df, left_index=True, right_index=True)

    # Output predicted point and player name to new csv file 
    final_prediction.to_csv(rf"data\\ML_prediction_{pos}.csv", encoding='utf-8-sig')



#position_ML_lr("data\\all_seasons_FWD_normalized.csv", "FWD")
#position_ML_lr("data\\all_seasons_MID_normalized.csv", "MID")
#position_ML_lr("data\\all_seasons_DEF_normalized.csv", "DEF")
#position_ML_lr("data\\all_seasons_GK_normalized.csv", "GK")