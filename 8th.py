# Convert the Centigrade degrees NumPy array into Fahrenheit degrees. Here is the formula to
# convert:

import numpy as np

cel = np.array([0, 12, 45.21, 34, 99.91])
print(cel)

far = (9 * cel / 5 + 32)
print(far)
