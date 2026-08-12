import numpy as np

'''
1-D: arr[element]
2-D: arr[rows, columns]
3-D: arr[layers, rows, columns]
'''

# Indexing a 1-D Array
"""arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[2])
print(arr[4])"""

# ----------------------------------//------------------------------------//

# Slicing a 1-D Array
# arr[start:stop]
"""
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])"""
# Ex:
'''
print(arr[:3])
Start defaults to 0.

print(arr[3:])
Goes from index 3 to the end.

print(arr[:])
Returns the whole array.'''

# ----------------------------------//------------------------------------//

# Slicing a 2-D Array
"""arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr[1])
print(arr[:, 2])"""
# print(arr[1])-->prints '1' indexed row.
'''
print(start(including):stop(excluding),start(including):stop(excluding))
      \______________________________/^\______________________________/
                       ^              |                ^
                       |              |                |
                       |              |                |
                rows operations   seperation    column operations
'''

# ---------------------------------//-------------------------//

# Slicing a 3-D Array
'''arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr[0, 1, 1])'''
# syntax
'''
arr[layer_start:layer_stop,
row_start:row_stop,
column_start:column_stop]
'''
# Visual representation:
'''
print(arr[layer, row, column])

|--------- Layers ---------||---------- Rows ----------||-------- Columns --------|
    start     :    stop          start      :    stop         start      :    stop
 (Included)     (Excluded)    (Included)      (Excluded)    (Included)      (Excluded)

                ↓                       ↓                            ↓
print(arr[layer_selection,          row_selection,             column_selection])

            Layer                         Row                       Column
'''

# ---------------------------------//-------------------------//

# Negative Slicing
"""arr = np.array([10, 20, 30, 40, 50])
print(arr[-1])   # output:50
print(arr[-2:])  # output:[40 50]
print(arr[:-1])  # output:[10 20 30 40]"""
# print(arr[start:stop])

# Indexes
'''
Positive
  0   1   2   3   4
[10, 20, 30, 40, 50]

Negative
 -5  -4  -3  -2  -1
[10, 20, 30, 40, 50]
'''

# ---------------------------------//-------------------------//
