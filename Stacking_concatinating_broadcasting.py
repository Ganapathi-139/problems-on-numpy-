'''
What is Stacking?
Stacking means placing arrays on top of each other or side by side.
'''

import numpy as np

# Part A: Stacking ndarrays

# stack(np.stack())
"""arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.stack((arr1, arr2))
print(result)"""

# 1. Vertical Stacking (np.vstack())
# '.vstack()' is used to convert given arrays into vertical stack

"""arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])
result = np.vstack((arr1, arr2))
print(result)"""

# 2. Horizontal Stacking (np.hstack())
# '.hstack()' is used to convert given arrays into horizontal stack

"""arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])
result = np.hstack((arr1, arr2))
print(result)"""

# Part B: Concatenating ndarrays

# 3: Concatenate Along Rows (axis=0)
"""arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])
result = np.concatenate((arr1, arr2), axis=0)
print(result)"""

# 4: Concatenate Along Columns (axis=1)
"""arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])
result = np.concatenate((arr1, arr2), axis=1)
print(result)"""

# Part C: Broadcasting with arrays
"""arr1 = np.array([[1],
                 [2],
                 [3]])
arr2 = np.array([10, 20, 30])
result = arr1+arr2
print(result)"""
