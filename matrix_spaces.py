import sympy as sp

# Basis for 2x2 symmetric matrices

B1 = sp.Matrix([
    [1, 0],
    [0, 0]
])

B2 = sp.Matrix([
    [0, 1],
    [1, 0]
])

B3 = sp.Matrix([
    [0, 0],
    [0, 1]
])

a = 3
b = 5
c = -2

A = a * B1 + b * B2 + c * B3

print("Constructed symmetric matrix:")
sp.pprint(A)

symmetric_basis = [B1, B2, B3]

print("Basis for symmetric 2x2 matrices:")

for matrix in symmetric_basis:
    sp.pprint(matrix)
    print()

print("Dimension:", len(symmetric_basis))