import numpy as np

A = np.array([
    [2., 1.],
    [6., 5.]
])

m = A[1, 0] / A[0, 0]

L = np.array([
    [1., 0.],
    [m, 1.]
])

U = np.array([
    [A[0, 0], A[0, 1]],
    [0., A[1, 1] - m * A[0, 1]]
])

print("L:")
print(L)

print("U:")
print(U)

print("LU:")
print(L @ U)

print("Original A:")
print(A)