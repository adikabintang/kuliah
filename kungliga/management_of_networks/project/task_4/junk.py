from random import choices
from collections import Counter
import numpy

population = [1, 2, 3, 4, 5, 6]
weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
#million_samples = choices(population, weights, k=10**4)
# print(million_samples)
#print(Counter(million_samples))

# t = [18]
# p = [0.64]
# hm = choices(t, p, k=1080)
# print(Counter(hm))

p = 0.8
arr = []
for i in range(0, 1080):
    v = numpy.random.uniform(low=0.0, high=1.0)
    arr.append(1 if v < p else 0)

m = Counter(arr)
print(m)
print(m[1])