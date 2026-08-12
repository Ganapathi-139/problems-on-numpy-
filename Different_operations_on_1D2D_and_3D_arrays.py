# import numpy as np  # importing numpy globally

# Problem 1: Dimensions of a NumPy Array(ndim)
# 1-D Array (One Dimension)
"""
[10 20 30 40]
"""

# 2-D Array (Two Dimensions)
"""
[
 [1 2 3]
 [4 5 6]
]
"""

# 3-D Array (Three Dimensions)
"""
[
 [
  [1 2]
  [3 4]
 ]

 [
  [5 6]
  [7 8]
 ]
]
"""

# 'ndim' is a key word to check the dimentions of an array

# Example program for checking dimention of an array
"""arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(f"Dimention: {arr.ndim}")"""

# Problem 2: Shape of a NumPy Array (shape)
"""arr = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr)
print(f"Shape of array: {arr.shape}")"""

# Problem 3: Size of a NumPy Array (size)
"""arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
print(f"Size of array: {arr.size}")"""

# Problem 4: Reshape an Array (reshape)
"""arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Before reshape: {arr}\n")
new_arr = arr.reshape(2, 3)
print(f"After reshape:\n{new_arr}")"""

# Problem 5: Flatten a NumPy Array (flatten)
"""arr = np.array([[1, 2, 3],
                [4, 5, 6]])
flat = arr.flatten()
print(f"Flatten array: {flat}")"""

# Problem 6: Transpose (.T)
"""arr = np.array([[1, 2, 3],
                   [4, 5, 6]])
trans = arr.T
print(f"Transpose array: {trans}")"""
