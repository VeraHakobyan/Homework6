# 1. For the given NumPy array find all complex and real numbers. Also test whether a given
# number is a scalar type or not.

import numpy as np
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array", a)

print("Complex numbers", np.iscomplex(a))

print("Real numbers", np.isreal(a))
print(np.isscalar(5.2))
