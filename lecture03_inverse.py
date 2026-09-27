import numpy as np

A = np.array([
    [2., 1.],
    [1., 1.]
])

A_inv = np.linalg.inv(A)

print("A inverse:")
print(A_inv)

print("Check:")
print(A @ A_inv)