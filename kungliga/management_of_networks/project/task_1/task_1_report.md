Adika Bintang Sulaeman

19940715-­T696 

# 1 Statistics

Key functions for getting the statistics:

```python
max() # get max value from the dataframe
mean() # get mean of the dataframe
min() # get min value from the dataframe
std() # get standard deviation of the dataframe
quantile(percentage) # get quantile from the dataframe
```

For the function `quantile`, the parameter `percentage` is for the percentage of the quantile. For example, 0.25 means 25th percentile.

I also used `X.loc[:, X.columns != 'TimeStamp']` to exclude `TimeStamp` from the calculation. `np.round` is used to round the floating number.

# 2 filtering data

We can filter data using conditionals. In the task 1, `X[X["all_%%usr"] < 90]` filters the data to take only rows with `X["all_%%usr"]` less than 90. Then, we can count the number of observations (or row of the csv) using `count()` function.

# 3 plotting

To change the index from `0 1 2 ...` to the timestamp, we replace the index with the timestamp from the table.

```python
timeIndex = pd.to_datetime(X['TimeStamp'], unit='s')
X.index = timeIndex
```

function `fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 4))` is used to create a figure which the plot will be on.

function `dataframe.plot(**kwargs)` is used to plot the dataframe. The `kwargs` can contain other parameters such as setting the line color.

`axes.grid(True)` draws the grid.

`matplotlib.plt.xlabel()` and `ylabel()` sets the labels for the axes.

`dataframe.boxplot(column = array of column name)` is used for creating boxplot.

`dataframe.plot.kde()` is used to create the density plot.

To create histogram, we need to create the bins. The bins is the difference between the max value and the min value of the dataframe. For example, the bins for memory usage is:

```python
memused_bins = int(X['%%memused'].max() - X['%%memused'].min())
```

Then, we can create the histogram using `hist` function. Example of histogram for memory usage:

```python
axes[0].hist(X['%%memused'], bins = memused_bins, color='b')
```