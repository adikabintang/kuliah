import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np


X = pd.read_csv('data/X.csv')
Y = pd.read_csv('data/Y.csv')
Y['TimeStamp'] = Y.TimeStamp.astype(int)

X.index = pd.to_datetime(
    X['TimeStamp'], unit='s')
Y.index = pd.to_datetime(
    Y['TimeStamp'], unit='s')

print(X.head())
print(Y.head())

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.7)

# print("------ 2")
# print(X_train.merge(Y.drop(['TimeStamp'], axis=1), left_index=True, right_index=True).head())

# Labeling the y_training
y_train_sla_label = np.array(
    y_train['DispFrames'] >= 18.0).astype(int)

logisticRegr = LogisticRegression(C=1e5, solver='lbfgs', 
    multi_class='multinomial')

X_train = X_train.drop(['TimeStamp'], axis=1)
logisticRegr.fit(X_train, y_train_sla_label)

# lol = X_test.merge(y_test.drop(['TimeStamp'], axis=1), left_index=True, right_index=True)
# lol['r'] = np.array(r)

for idx, col_name in enumerate(X_train.columns):
    print("{} The coefficient for {} is {}".format(idx+1, col_name,
                                                   np.round(logisticRegr.coef_[0][idx], decimals=3)))

intercept = np.round(logisticRegr.intercept_[0], decimals=3)
print("The intercept for our model is (teta 0) {}".format(intercept))

# (2)

prediction_result = logisticRegr.predict(X_test.drop(['TimeStamp'], axis=1))
print("prediction result")
print(prediction_result)
y_test_merged = y_test.copy()
y_test_merged['predicted_sla'] = np.array(prediction_result)

print(y_test_merged.head(7))

# https://developers.google.com/machine-learning/crash-course/classification/true-false-positive-negative
# TP: bilang ya, bener ya
# TN: bilang ngga, bener ngga
# FP: bilang ya, padahal ngga
# FN: bilang ngga, padahal ya

# compute the confusion matrix, which includes the four numbers 
# True Positives (TP), True Negatives (TN), False Positives (FN), 
# and False Negatives (FN)
arr = []
y_true = []
TP = 0
TN = 0
for idx, row in y_test_merged.iterrows():
    # sum_abs_y_mean_predict += abs(row['DispFrames'] - y_predict[i][0])
    # i += 1
    if row['predicted_sla'] == 1:
        if row['DispFrames'] >= 18.0:
            TP += 1
            arr.append('TP')
        else:
            #FP += 1
            arr.append('FP')
    else:
        if row['DispFrames'] < 18.0:
            TN += 1
            arr.append('TN')
        else:
            #FN += 1
            arr.append('FN')
    
    if row['DispFrames'] >= 18.0:
        y_true.append(1)
    else:
        y_true.append(0)
        
y_test_merged['classification_error'] = np.array(arr)
print(y_test_merged.head(10))

err = 1 - (TP + TN) / len(y_test_merged.index)
print("err: {}".format(err))

from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

# fig, ax = plt.subplots()
# im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
# plt.show()

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    
    classes = classes[unique_labels(y_true.astype(int), y_pred.astype(int))]

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

class_names = np.array([0, 1]).astype(int)
cm = confusion_matrix(y_true, prediction_result)
print(cm)
print(prediction_result)
print(np.array(y_true).astype(int))
# Plot non-normalized confusion matrix
plot_confusion_matrix(np.array(y_true), prediction_result, classes=class_names,
                      title='Confusion matrix, without normalization')
# plt.show()

# (3) naive

sla_conform = len(y_train[y_train['DispFrames'] >= 18.0].index)
print("sla_conform: {}".format(sla_conform))
print("all: {}".format(len(y_train.index)))
p = sla_conform / len(y_train.index)
print("p: {}".format(p))

# (4) 

from sklearn.linear_model import LinearRegression

regression_model = LinearRegression()
regression_model.fit(X_train, y_train.drop(['TimeStamp'], axis=1))
print(y_train.drop(['TimeStamp'], axis=1))
print("aaaa")
#print((X_test.drop(['TimeStamp'], axis=1)))
y_predict_4 = regression_model.predict(X_test.drop(['TimeStamp'], axis=1))
print(y_predict_4)
print(np.array(np.where(y_predict_4 >= 18.0, 1, 0)).flatten())