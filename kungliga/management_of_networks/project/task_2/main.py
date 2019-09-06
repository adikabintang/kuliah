# http://benalexkeen.com/linear-regression-in-python-using-scikit-learn/
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

X = pd.read_csv('data/X.csv')
Y = pd.read_csv('data/Y.csv')
Y['TimeStamp'] = Y.TimeStamp.astype(int)

joined_dataframe = X.merge(Y, on=['TimeStamp'], how='inner')
# print(joined_dataframe.head())

x = joined_dataframe.drop(['TimeStamp', 'DispFrames'], axis = 1)
y = joined_dataframe[['DispFrames']]

# print("---")
# print(x.head())
# print("+++")
# print(y.head())

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

for idx, col_name in enumerate(X_train.columns):
    print("{} The coefficient for {} is {}".format(idx+1, col_name, 
        np.round(regression_model.coef_[0][idx], decimals=3)))

intercept = np.round(regression_model.intercept_[0], decimals=3)
print("The intercept for our model is (teta 0) {}".format(intercept))