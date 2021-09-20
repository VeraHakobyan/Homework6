# 5. Create a n-sized vector with random numbers from normal distribution and reverse it.
import numpy as np

n = int(input())
arr = np.random.normal(0, 10, n)
print(arr)
arr_reversed = arr[::-1]
print(arr_reversed)
