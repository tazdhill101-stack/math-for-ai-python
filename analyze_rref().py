import sympy as sp

A = sp.Matrix([
    [1, 2, 3, 4],
    [2, 4, 7, 9],
    [1, 2, 4, 5]
])

rref_A, pivot_columns = A.rref()

print("RREF:")
print(rref_A)

print("Pivot columns:")
print(pivot_columns)