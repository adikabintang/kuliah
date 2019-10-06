# Report Task 4

## Optimal Method

```
The smallest NMAE (0.08975443) is the model with features: 'runq-sz', '%%memused', 'cswch/s', 'all_%%usr', 'totsck', 'pgfree/s', 'plist-sz', 'file-nr', 'idel/s'.
```

![historgram_nmae_opt.png](historgram_nmae_opt.png)

![boxplot_nmae_opt.png](boxplot_nmae_opt.png)

The method which is used to find the features with the smallest error is building a subset of each features, building the linear regression model, then finding the smallest NMAE of all the models built. The features with the smallest error are 'runq-sz', '%%memused', 'cswch/s', 'all_%%usr', 'totsck', 'pgfree/s', 'plist-sz', 'file-nr', 'idel/s'.

From the histogram, we can see the the highest number of error (NMAE) is aronud 0.1 with more than 2500 data. This means that the models mostly have 0.1 error with various features applied to the model.

The boxplot shows the relation between the number of features and the NMAE. The growth of the function resembles the inverse logarithmic function, with the NMAE seems to saturate when the number of features exceeds 4.

## Heuristic method

```
Rank of the features according to the square of the correlation values:
plist-sz: 0.6425110620330668
totsck: 0.6393556902902942
runq-sz: 0.6347416660198467
ldavg-1: 0.6220876144130324
cswch/s: 0.5450026386364569
file-nr: 0.5302460329240475
all_%%usr: 0.3174976699613216
%%memused: 0.11999712957104583
idel/s: 0.06539338495183551
proc/s: 0.042141726713423186
pgfree/s: 0.0007517512284019827
tps: 1.94979764922491e-05
```

![error_heuristic.png](error_heuristic.png)

The correlation values calculated is within the range [-1, +1]. The rank of the correlation values presented is the square of the correlation values, which means all features ranked is positive values. By ranking the square of the correlation values, it is expected to see how each features contribute to the estimated values.

The abosulte correlation value indicates the strength of the relation ship, while the sign of the value shows the direction of the relationship [1].

This heuristic method also shows how many features we need to build such a reliable model in a heuristic way. If the number of features included in a model is less then 6, the NMAE is relatively high. If the number of features is more than 6, the NMAE is steeply reduced. We can say that 8 features is the good number of features to build a model, whereas if we give more than 8, it will not significantly improve the model. The method shows that we need 8 features at least, which are plist-sz, totsck, runq-sz, ldavg-1, cswch/s, file-nr, all_%%usr, %%memused, to build a reliable model.

## Correlation matrix showing the correlation between variable

![correlation_matrix.png](correlation_matrix.png)

According to the optimal method, the smallest NMAE is given by a model built with 9 features: 'runq-sz', '%%memused', 'cswch/s', 'all_%%usr', 'totsck', 'pgfree/s', 'plist-sz', 'file-nr', 'idel/s'. These 9 features has correlation values of:

- 'runq-sz': -0.796706
- '%%memused': 0.346406
- 'cswch/s': -0.73824
- 'all_%%usr': -0.563469
- 'totsck': -0.799597
- 'pgfree/s': 0.027418
- 'plist-sz': -0.801568
- 'file-nr': -0.72818
- 'idel/s': -0.25572

As we discussed, the absolute value of the correlation shows the strength while the sign gives the direction. The feature `run-qz`, `cswch/s`, `file-nr`, and `totsck` have high correlation values and affect the target in negative relationship. While those features highly affect the model, the `pgfree/s` feature has very small correlation value, which means it does not really affect the result of the model calculation.

The heuristic method in part 3 selects the features based on the ranking of the squared correlation values (we can also easily infer that this means the absolute values that we are considering). This method tries to find the best model built for each k features by choosing the most correlated features.

## Comparison of the optimal method with the heuristic method

![comparison](comparison.png)

The curves show the relationship between the number of features and the error values. For every model built with 1 to 11 features, the error of optimal method is smaller than those of heuristic method. This means that optimal method gives more precise model than the heuristic model, which is expected. Heuristic focuses more on reaching immediate goal yet not guaranteed to be optimal or perfect [2].

Another thing to see from the graph is when the model generates smaller errors. With the optimal method, even with only 4 features, it can build a model with smaller errors. In heuristic method, only models with more than 6 features has smaller error values.

The optimal method tries to find the most correlated features by brute forcing, creating different models with all combinations of all features. This is very exhausting task yet guaranteed to find the best model. On the other hand, heuristic model tries to calculate the correlation value and determine what features it will take based on the result of the correlation values calculation.

#### Conclusion

- The optimal method is slower, with the growth function of O(2^n), while heuristic method is faster, with the growth function of O(n)
- The optimal method is more accurate than the heuristic method to find the most correlated features to build the model
- If the number of features are relatively small, than optimal method can be used. If the number of features are high, then heuristic method is preferable. However, the trade-offs between accuracy and efficiency must be taken into account.

## References

[1] https://statisticsbyjim.com/basics/correlations/

[2] https://en.wikipedia.org/wiki/Heuristic