from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd
import numpy as np
import all_seasons as wb

def points_regression_model(directory):

    df = wb.extract_df_dir(directory)

    # Create X and Y dataframes
    X = df.iloc[:,[5,6,10,11,12,13,14,15,20,21]]
    Y = df.iloc[:,[9]]

    # Replace nan float values with 0 in the X and Y dataframes
    X = X.replace(np.nan, 0)
    Y = Y.replace(np.nan, 0)

    # Split data into 80% test and 20% train 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # Create the model
    model = linear_model.LinearRegression()
    # Apply the training data to the model
    model.fit(X_train, Y_train)

    # Create the predicted total points from the 20% testing data
    Y_pred = model.predict(X_test)

    print("Coefficients: ", model.coef_[0], "\n")
    # "%.2f" puts proceeding number to 2 decimal places
    print("Intercept: ", model.intercept_, "\n")
    print("Mean Squared Error (MSE): %.2f" % mean_squared_error(Y_test, Y_pred), " \n")
    print("Coefficient of determination (R^2): %.2f" % r2_score(Y_test, Y_pred)," \n")

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