import numpy as np

A = np.array([
    [2., 1.],
    [6., 5.]
])

multiplier = A[1, 0] / A[0, 0]

A[1] = A[1] - multiplier * A[0]

print("Multiplier:", multiplier)
print("Upper triangular matrix:")
print(A)