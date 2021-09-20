# 3. Create a NumPy array of 10 zeros,10 ones, 10 fives.

import numpy as np

arr_zeros = np.zeros(10, dtype=int)
arr_ones = np.ones(10, dtype=int)
arr_fives = arr_ones * 5

print(arr_zeros)
print(arr_ones)
print(arr_fives)
