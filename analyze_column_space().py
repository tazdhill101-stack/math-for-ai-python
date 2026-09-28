import sympy as sp

A = sp.Matrix([
    [1, 2, 1, 3],
    [2, 4, 2, 6],
    [0, 0, 1, 2]
])

column_basis = A.columnspace()

print("Basis for column space:")

for vector in column_basis:
    print(vector)