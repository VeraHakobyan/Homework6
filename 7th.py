# 7. Create a square NumPy matrix and fill it with a checkerboard pattern.

import numpy as np

x = np.zeros((8, 8), dtype=int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
print(x)
