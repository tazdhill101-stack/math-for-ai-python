import numpy as np

# Matrix A
A = np.array([
    [1, 2],
    [3, 4]
])

# Vector b
b = np.array([5, 11])

# Solve Ax = b
x = np.linalg.solve(A, b)

# Check the answer
check = A @ x

print("Matrix A:")
print(A)

print("\nVector b:")
print(b)

print("\nSolution x:")
print(x)

print("\nCheck Ax:")
print(check)