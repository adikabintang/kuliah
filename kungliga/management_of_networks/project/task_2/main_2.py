# http://benalexkeen.com/linear-regression-in-python-using-scikit-learn/
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

def get_nmae(y_predict, y_test):
    m = y_test['DispFrames'].count()
    y_mean = y_test['DispFrames'].mean()
    y_predict = regression_model.predict(X_test)

    sum_abs_y_mean_predict = 0.0
    i = 0
    for _, row in y_test.iterrows():
        # print("{} - {}".format(row['DispFrames'], y_predict[i][0]))
        sum_abs_y_mean_predict += abs(row['DispFrames'] - y_predict[i][0])
        i += 1

    nmae = (sum_abs_y_mean_predict / m) / y_mean
    return np.round(nmae, decimals=8)

X = pd.read_csv('data/X.csv')
Y = pd.read_csv('data/Y.csv')
Y['TimeStamp'] = Y.TimeStamp.astype(int)

joined_dataframe = X.merge(Y, on=['TimeStamp'], how='inner')
# print(joined_dataframe.head())

x = joined_dataframe.drop(['TimeStamp', 'DispFrames'], axis=1)
y = joined_dataframe[['DispFrames']]
training_test_sizes = [50, 100, 200, 500, 1000, 2520]

x_train_ori, x_test_ori, y_train_ori, y_test_ori = train_test_split(x, y,
                                                                train_size=0.7)

d = {}
m = {}
for train_size in training_test_sizes:
    nmaes = []
    mse = []
    for i in range(0, 50):
        X_train, X_test, y_train, y_test = train_test_split(x, y,
                                                            train_size=train_size)
        regression_model = LinearRegression()
        regression_model.fit(X_train, y_train)

        y_predict = regression_model.predict(x_test_ori)
        
        nmaes.append(get_nmae(y_predict, y_test_ori))
        mse.append(mean_squared_error(y_predict, y_test_ori))

        # print("training size: {}, nmae: {}".format(train_size, nmae))
    
    d[train_size] = nmaes
    m[train_size] = mse

df = pd.DataFrame(data=d)
mf = pd.DataFrame(data=m)
plt.subplot(2, 1, 1)
mf.boxplot(column = training_test_sizes)
plt.subplot(2, 1, 2)
df.boxplot(column = training_test_sizes)
plt.show()