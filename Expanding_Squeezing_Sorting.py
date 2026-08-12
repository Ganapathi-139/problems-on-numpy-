import numpy as np

# Problem 1: Expanding a NumPy Array
# expand function is used to change dimentions(1-D array to 2-D array)
# when axis=0 is used add a new row
"""arr = np.array([10, 20, 30, 40])
expanded = np.expand_dims(arr, axis=0)
print(arr)
print(expanded)"""

# To Check the Dimensions
"""print(arr.ndim)
print(expanded.ndim)"""

# when axis=1 is used add a new column
"""arr = np.array([10, 20, 30, 40])
expanded = np.expand_dims(arr, axis=1)
print(arr)
print(expanded)"""
# To Check the Dimensions
"""print(arr.ndim)
print(expanded.ndim)"""
# ---------------------------------//-------------------------//
# Problem 2: Squeezing a NumPy Array
"""arr = np.array([[10, 20, 30, 40]])
squeezed = np.squeeze(arr)
print(arr)
print(squeezed)"""
# verify with .shape
"""print(arr.shape)
print(squeezed.shape)"""

# ---------------------------------//-------------------------//

# Problem 3: Sorting a NumPy Array
# Sorting a 1-D Array
"""arr = np.array([25, 10, 40, 5, 30])
sorted_arr = np.sort(arr)
print(sorted_arr)"""

# Sorting a 2-D Array
"""arr = np.array([[30, 20, 10],
                [60, 50, 40]])
print(np.sort(arr))"""
