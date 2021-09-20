# 6. Add a border with zeros to the given square NumPy matrix.

import numpy as np

# n = int(input())

arr = np.ones((3, 3), dtype=int)
print(arr)

border_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print(border_arr)
