import sympy as sp

A = sp.Matrix([
    [1, 2, 3],
    [2, 4, 7],
    [1, 2, 4]
])

print("Matrix A:")
sp.pprint(A)

# Column space
column_space = A.columnspace()

print("\nBasis for column space:")

for vector in column_space:
    sp.pprint(vector)

print("\nDimension of column space:")
print(len(column_space))

# Nullspace
null_space = A.nullspace()

print("\nBasis for nullspace:")

for vector in null_space:
    sp.pprint(vector)

print("\nDimension of nullspace:")
print(len(null_space))

# Rank-nullity check
rank = A.rank()
number_of_columns = A.shape[1]
nullity = len(null_space)

print("\nRank:", rank)
print("Nullity:", nullity)

print(
    "Rank + Nullity =",
    rank + nullity
)

print(
    "Number of columns =",
    number_of_columns
)