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

X = pd.read_csv('data/X.csv')
Y = pd.read_csv('data/Y.csv')
Y['TimeStamp'] = Y.TimeStamp.astype(int)
X.index = pd.to_datetime(
    X['TimeStamp'], unit='s')
Y.index = pd.to_datetime(
    Y['TimeStamp'], unit='s')

feature_names = ["runq-sz", "%%memused", "proc/s", "cswch/s", "all_%%usr", 
    "ldavg-1", "totsck", "pgfree/s", 
    "plist-sz", "file-nr", "idel/s", "tps"]
all_subset = subs(feature_names)

# all_subset = subs(["runq-sz", "%%memused"])

# all_nmae = []
# nmaes_boxplot_data = []
# for subset in all_subset:
#     x_train, x_test, y_train, y_test = train_test_split(X[subset], 
#         Y[["DispFrames"]], train_size=0.7)
#     regression_model = LinearRegression()
#     regression_model.fit(x_train, y_train)
#     y_predict = regression_model.predict(x_test)
#     nmae = get_nmae(y_predict, y_test)
#     all_nmae.append(nmae)
    
#     if len(nmaes_boxplot_data) < len(subset):
#         nmaes_boxplot_data.append([nmae])
#     else:
#         nmaes_boxplot_data[len(subset) - 1].append(nmae)

# min_nmae = min(all_nmae)
# print("the smallest name is the model with features:")
# print(all_subset[all_nmae.index(min_nmae)])

# binwidth = 0.01
# print(all_nmae)
# plt.hist(all_nmae, 
#     bins=np.arange(min(all_nmae), max(all_nmae) + binwidth, binwidth))
# plt.show()

# fig7, ax7 = plt.subplots()
# ax7.set_title('Multiple Samples with Different sizes')
# ax7.boxplot(nmaes_boxplot_data)
# plt.show()

# (3)

x_train, x_test, y_train, y_test = train_test_split(X, 
        Y[["DispFrames"]], train_size=0.7)

m = len(x_train.index)

correlation_square_map = {}
correlation_map = {}
for feature in feature_names:
    x_mean = x_train[feature].mean()
    y_mean = y_train["DispFrames"].mean()
    x_std = x_train[feature].std()
    y_std = y_train["DispFrames"].std()
    sum_all = 0.0
    
    for idx, xi in x_train.iterrows():
        sum_all += ((xi[feature] - x_mean) * (y_train["DispFrames"][idx])) \
            / (x_std * y_std)
    
    correlation = sum_all / m
    correlation_square_map[feature] = correlation ** 2
    correlation_map[feature] = correlation
    
sorted_correlation_sq_tuple = sorted(correlation_square_map.items(), key=lambda kv: kv[1],
    reverse=True)
sorted_feature = [feature[0] for feature in sorted_correlation_sq_tuple]
print("Rank of the features according to the square of the correlation values:")
for feature in sorted_feature:
    print(feature)

all_nmaes = []
for i in range(1, len(sorted_feature) + 1):
    regression_model = LinearRegression()
    regression_model.fit(x_train[sorted_feature[0:i]], y_train)
    y_predict = regression_model.predict(x_test[sorted_feature[0:i]])
    nmae = get_nmae(y_predict, y_test)
    all_nmaes.append(nmae)

plt.plot(range(1, 13), all_nmaes)
plt.show()

# (4)

sorted_correlation = sorted(correlation_map.items(), key=lambda kv: kv[1],
    reverse=True)
sorted_feature = [feature[0] for feature in sorted_correlation]
sorted_correlation = [[val[1]] for val in sorted_correlation]
plt.matshow(sorted_correlation, cmap='RdPu')
plt.colorbar()

y_pos = np.arange(len(sorted_correlation))
plt.yticks(y_pos, sorted_feature)

x_pos = [1]
plt.xticks(x_pos, ["DispFrames"])

plt.show()