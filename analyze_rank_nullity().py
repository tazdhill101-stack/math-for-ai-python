import sympy as sp

A = sp.Matrix([
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [0, 1, 1, 0, 2]
])

rank = A.rank()
nullspace = A.nullspace()
nullity = len(nullspace)

print("Number of columns:", A.cols)
print("Rank:", rank)
print("Nullity:", nullity)
print("Rank + nullity:", rank + nullity)

print("\nNullity:")
print(nullity)

print("\nRank + Nullity:")
print(rank + nullity)