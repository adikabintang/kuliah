# http://benalexkeen.com/linear-regression-in-python-using-scikit-learn/
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


def get_nmae(y_predict, y_test):
    m = y_test['DispFrames'].count()
    y_mean = y_test['DispFrames'].mean()
    y_predict = regression_model.predict(X_test)

    sum_abs_y_mean_predict = 0.0
    i = 0
    for _, row in y_test.iterrows():
        sum_abs_y_mean_predict += abs(row['DispFrames'] - y_predict[i][0])
        i += 1

    nmae = (sum_abs_y_mean_predict / m) / y_mean
    return np.round(nmae, decimals=8)


X = pd.read_csv('data/X.csv')
Y = pd.read_csv('data/Y.csv')
Y['TimeStamp'] = Y.TimeStamp.astype(int)

joined_dataframe = X.merge(Y, on=['TimeStamp'], how='inner')
joined_dataframe.index = pd.to_datetime(
    joined_dataframe['TimeStamp'], unit='s')

x = joined_dataframe.drop(['TimeStamp', 'DispFrames'], axis=1)
y = joined_dataframe[['DispFrames']]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)
y_predict = regression_model.predict(X_test)


for idx, col_name in enumerate(X_train.columns):
    print("{} The coefficient for {} is {}".format(idx+1, col_name,
                                                   np.round(regression_model.coef_[0][idx], decimals=3)))

intercept = np.round(regression_model.intercept_[0], decimals=3)
print("The intercept for our model is (teta 0) {}".format(intercept))

## 1 (b)

print("nmae of the model: {}".format(get_nmae(y_predict, y_test)))
y_test_mean = y_test['DispFrames'].mean()  # for naive prediction
print("y_test_mean: {}".format(y_test_mean))

# 1 (c)

joined_result = y_test.copy()
joined_result['predict'] = y_predict
joined_result['naively_predict'] = np.full((y_test['DispFrames'].count(), 1),
                                           y_test_mean)
print(joined_result.head())
joined_result['DispFrames'].plot(color='blue')
joined_result['predict'].plot(color='red')
joined_result['naively_predict'].plot(color='green')
plt.legend(('actual frames', 'predicted frames', 'naively predicted frames'),
           loc='lower right', shadow=False, fancybox=True)
plt.show()

# 1 (d)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))
n_bins = int(y_test['DispFrames'].max() - y_test['DispFrames'].min())
axes[0].hist(y_test['DispFrames'], bins=n_bins, color='b')
y_test['DispFrames'].plot.kde(ind=np.linspace(0, 140, 139), color='r')
plt.tight_layout()
plt.show()

# 1 (e)
a = [1, 2, 3]
joined_result['estimation_errors'] = np.array(
    [(row['DispFrames'] - row['predict'])
        for _, row in joined_result.iterrows()])

joined_result['estimation_errors'].plot()
plt.show()
print(joined_result.head())