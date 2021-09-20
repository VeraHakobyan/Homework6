# 10. Write a NumPy program to find equal values between two arrays.

import numpy as np


arr1 = np.array([0, 5, 10, 15, 20])
print(arr1)
arr2 = [5, 15, 25]
print(arr2)
print("Common values between two arrays:")
print(np.intersect1d(arr1, arr2))
