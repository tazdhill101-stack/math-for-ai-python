import numpy as np

u = np.array([1, 2, -1])
v = np.array([3, 4])

A = np.outer(u, v)

print("u:")
print(u)

print("\nv:")
print(v)

print("\nRank-1 matrix A = uv^T:")
print(A)

print("\nRank of A:")
print(np.linalg.matrix_rank(A))