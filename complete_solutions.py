import sympy as sp

A = sp.Matrix([
    [1, 2, 1, 3],
    [2, 4, 3, 7],
    [1, 2, 2, 4]
])

b = sp.Matrix([2, 5, 3])

# RREF
rref_A, pivot_columns = A.rref()

print("RREF:")
sp.pprint(rref_A)

print("\nPivot columns:")
print(pivot_columns)

print("\nRank:")
print(A.rank())