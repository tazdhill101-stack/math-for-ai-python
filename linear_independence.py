import sympy as sp

v1 = sp.Matrix([1, 2, 3])
v2 = sp.Matrix([2, 4, 6])
v3 = sp.Matrix([1, 0, 1])

# Put vectors into columns of a matrix
A = sp.Matrix.hstack(v1, v2, v3)

print("Matrix:")
sp.pprint(A)

print("\nRREF:")
sp.pprint(A.rref()[0])

print("\nRank:")
print(A.rank())

print("\nNullspace:")
for vector in A.nullspace():
    sp.pprint(vector)

number_of_vectors = A.shape[1]

if A.rank() == number_of_vectors:
    print("\nThe vectors are linearly independent.")
else:
    print("\nThe vectors are linearly dependent.")