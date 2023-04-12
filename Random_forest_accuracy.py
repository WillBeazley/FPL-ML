from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score, classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import all_seasons as wb
from sklearn.metrics import r2_score, mean_squared_error

def points_regression_model(directory):

    df = wb.extract_df_dir(directory)

    # Create X and Y dataframes
    X = df.iloc[:,[5,10,11,12,13,14,15,20,21,22]]
    Y = df.iloc[:,[9]]

    # Replace nan float values with 0 in the X and Y dataframes
    X = X.replace(np.nan, 0)
    Y = Y.replace(np.nan, 0)

    # Split data into 80% test and 20% train 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # Split data into 80% test and 20% train
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    regressor = RandomForestRegressor(n_estimators=20, random_state=0)
    regressor.fit(X_train, Y_train.values.ravel())
    Y_pred = regressor.predict(X_test)

    mse = mean_squared_error(Y_test, Y_pred)

    print(f"Mean Squared Error (MSE):  {mse}")
    print(f"accuracy: {regressor.score(X_test, Y_test)}")

    # Convert predicted points np.array into a dataframe
    Y_pred_df = pd.DataFrame(Y_pred, columns=["total_points"])

print("FORWARDS:")
points_regression_model("data\\all_seasons_FWD_normalized.csv")
print("\nMIDFIELDERS:")
points_regression_model("data\\all_seasons_MID_normalized.csv")
print("\nDEFENDERS:")
points_regression_model("data\\all_seasons_DEF_normalized.csv")
print("\nGOALKEEPERS:")
points_regression_model("data\\all_seasons_GK_normalized.csv")