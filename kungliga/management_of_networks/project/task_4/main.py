import itertools
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def subs(l):
    res = []
    for i in range(1, len(l) + 1):
        for combo in itertools.combinations(l, i):
            res.append(list(combo))
    return res

def get_nmae(y_predict, y_test):
    m = len(y_test.index)
    y_mean = y_test['DispFrames'].mean()
    sum_abs_y_mean_predict = 0.0
    i = 0
    for _, row in y_test.iterrows():
        sum_abs_y_mean_predict += abs(row['DispFrames'] - y_predict[i][0])
        i += 1
    
    nmae = (sum_abs_y_mean_predict / m) / y_mean
    return np.round(nmae, decimals=8)

# all_subset = subs(["runq-sz", "%%memused", "proc/s", "cswch/s", "all_%%usr", 
#     "ldavg-1", "totsck", "pgfree/s", 
#     "plist-sz", "file-nr", "idel/s", "tps"])

all_subset = subs(["runq-sz", "%%memused", "proc/s", "cswch/s"])

X = pd.read_csv('data/X.csv')
Y = pd.read_csv('data/Y.csv')
Y['TimeStamp'] = Y.TimeStamp.astype(int)
X.index = pd.to_datetime(
    X['TimeStamp'], unit='s')
Y.index = pd.to_datetime(
    Y['TimeStamp'], unit='s')

all_nmae = []
nmaes_boxplot_data = []
for subset in all_subset:
    x_train, x_test, y_train, y_test = train_test_split(X[subset], 
        Y[["DispFrames"]], train_size=0.7)
    regression_model = LinearRegression()
    regression_model.fit(x_train, y_train)
    y_predict = regression_model.predict(x_test)
    nmae = get_nmae(y_predict, y_test)
    all_nmae.append(nmae)
    
    if len(nmaes_boxplot_data) < len(subset):
        nmaes_boxplot_data.append([nmae])
    else:
        nmaes_boxplot_data[len(subset) - 1].append(nmae)

min_nmae = min(all_nmae)
print("the smallest name is the model with features:")
print(all_subset[all_nmae.index(min_nmae)])

binwidth = 0.01
print(all_nmae)
# plt.hist(all_nmae, 
#     bins=np.arange(min(all_nmae), max(all_nmae) + binwidth, binwidth))
# plt.show()

fig7, ax7 = plt.subplots()
ax7.set_title('Multiple Samples with Different sizes')
ax7.boxplot(nmaes_boxplot_data)
plt.show()
