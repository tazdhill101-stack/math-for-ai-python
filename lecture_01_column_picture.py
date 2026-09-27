import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

x = np.array([2, 1])

column_1 = A[:, 0]
column_2 = A[:, 1]

result = x[0] * column_1 + x[1] * column_2

print("Column 1:")
print(column_1)

print("\nColumn 2:")
print(column_2)

print("\nLinear combination:")
print(result)

print("\nMatrix multiplication Ax:")
print(A @ x)
