# 2. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less
# and less_equal) of two given arrays.

import numpy as np

arr1 = np.random.randint(1, 1000, 5)
arr2 = np.random.randint(1, 1000, 5)

print(arr1)
print(arr2)

if (arr1 > arr2).all():
    print("All elements of arr1 is greater than those of arr2")
elif (arr1 >= arr2).all():
    print("All elements of arr1 is greater or equal than those of arr2")
elif (arr1 < arr2).all():
    print("All elements of arr1 is less than those of arr2")
elif (arr1 <= arr2).all():
    print("All elements of arr1 is less or equal than those of arr2")

