# Write a NumPy program to test whether each element of a 1-D array is also present in a
# second array.

import numpy as np
arr1 = np.array([5, 10, 15, 20, 25])
print(arr1)
arr2 = np.array([0, 10, 25])
print(arr2)
print("Compare each element of arr1 and arr2")
print(np.in1d(arr1, arr2))
