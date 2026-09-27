import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [2, 1],
    [0, 3]
])

print("Transpose:")
print(A.T)

print("(AB)^T:")
print((A @ B).T)

print("B^T A^T:")
print(B.T @ A.T)

print(
    "Are they equal?",
    np.allclose((A @ B).T, B.T @ A.T)
)