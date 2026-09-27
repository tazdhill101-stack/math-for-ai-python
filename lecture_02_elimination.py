import numpy as np

A = np.array([
    [2.0, 1.0],
    [6.0, 5.0]
])

print("Starting matrix:")
print(A)

multiplier = A[1, 0] / A[0, 0]

print("\nMultiplier:")
print(multiplier)

A[1] = A[1] - multiplier * A[0]

print("\nAfter elimination:")
print(A)