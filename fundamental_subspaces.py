import sympy as sp

A = sp.Matrix([
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 2]
])

print("Matrix A:")
sp.pprint(A)

# -------------------------
# Rank
# -------------------------

rank = A.rank()

print("\nRank:")
print(rank)

# -------------------------
# RREF
# -------------------------

rref_A, pivot_columns = A.rref()

print("\nRREF:")
sp.pprint(rref_A)

print("\nPivot columns:")
print(pivot_columns)

# -------------------------
# Column space
# -------------------------

column_space = A.columnspace()

print("\nBasis for column space:")

for vector in column_space:
    sp.pprint(vector)

# -------------------------
# Nullspace
# -------------------------

null_space = A.nullspace()

print("\nBasis for nullspace:")

for vector in null_space:
    sp.pprint(vector)

# -------------------------
# Row space
# -------------------------

row_space = A.rowspace()

print("\nBasis for row space:")

for vector in row_space:
    sp.pprint(vector)

# -------------------------
# Left nullspace
# -------------------------

left_null_space = A.T.nullspace()

print("\nBasis for left nullspace:")

for vector in left_null_space:
    sp.pprint(vector)

m, n = A.shape
r = A.rank()

column_space_dimension = r
row_space_dimension = r
nullspace_dimension = n - r
left_nullspace_dimension = m - r

print("\nDimensions")

print("Column space:", column_space_dimension)
print("Row space:", row_space_dimension)
print("Nullspace:", nullspace_dimension)
print("Left nullspace:", left_nullspace_dimension)

null_vectors = A.nullspace()

for x in null_vectors:

    print("\nNullspace vector:")
    sp.pprint(x)

    print("A*x:")
    sp.pprint(A * x)