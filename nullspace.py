import sympy as sp

A = sp.Matrix([
    [1, 2, 3],
    [2, 4, 6]
])

null_basis = A.nullspace()

print(null_basis)

for v in null_basis:
    print(A * v)