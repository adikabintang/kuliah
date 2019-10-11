# Part 1: How to read some basic plots

## How to read box plot and density plot

### Boxplot

- How to read boxplot [[towardsdatascience](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51#targetText=A%20boxplot%20is%20a%20standardized,and%20what%20their%20values%20are.)]

![boxplot](https://miro.medium.com/max/9000/1*2c21SkzJMf3frPXPAR_gZA.png)
Image source: Michael Galarnyk on [towardsdatascience](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51#targetText=A%20boxplot%20is%20a%20standardized,and%20what%20their%20values%20are.)

Boxplot shows:
- Median (Q2)
- Q1
- Q3
- The box is actually interquartile range (IQR) = `Q3 - Q1`
- Minimum (`Q1 - 1.5 * IQR`)
- Maximum (`Q1 + 1.5 * IQR`)
- Outliers: data that is very different from the others [[wikipedia](https://en.wikipedia.org/wiki/Outlier#targetText=In%20statistics%2C%20an%20outlier%20is,serious%20problems%20in%20statistical%20analyses.)]

### Density plot

What is density plot: [towardsdatascience.com](https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0).

- x values: like those of histogram
- y values: hmmm...

Some hints:
- The _area_ under the curve represents the probability of getting an x value between a range of x values [[stackexchange](https://stats.stackexchange.com/questions/48109/what-does-the-y-axis-in-a-kernel-density-plot-mean)]
- Watch this if the first point does not makes sense: [[khanacademy](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-continuous/v/probability-density-functions)]
- Another article: [[towardsdatascience](https://towardsdatascience.com/how-to-find-probability-from-probability-density-plots-7c392b218bab)]

# Part 2: Linear Regression

## How linear regression works

...

## When to use linear regression

...

## Error calculation

### Mean Squared Error (MSE) and Normalized Mean Absolute Error (NMAE)

...

### The relationship between the estimation error and training size

...

# Part 3: Classification - Logistic Regression

## How Logistic Regression Works

...

## Classification: True vs. False and Positive vs. Negative

https://developers.google.com/machine-learning/crash-course/classification/true-false-positive-negative

### Confusion Matrix

...

# Part 4: Reducing the features (X values)

## Optimal Method: Build all subsets of the feature set X

...

## Heuristic Method: Linear univariate feature selection

...

### Correlation Matrix

...

## Principle Component Analysis (PCA)

...

## When to use the optimal, heuristic, or PCA?

...
