# Linear Algebra in Python

A collection of Python implementations of fundamental linear algebra concepts, with a focus on developing the mathematical foundations used in AI and machine learning.

Overview

This repository documents my practical work with linear algebra using Python. Each file explores a different concept through calculations, examples, and implementations.

The aim is to combine mathematical understanding with programming and gradually build a portfolio of projects relevant to AI, machine learning, and data science.

Topics

Current implementations include:

* Systems of linear equations
* Gaussian elimination
* Row echelon form and reduced row echelon form (RREF)
* Matrix operations
* Matrix inverses
* LU decomposition
* Vector spaces
* Linear combinations
* Column spaces
* Null spaces
* Rank and pivot variables

More topics will be added as the repository develops.

Technologies

* Python
* NumPy
* SymPy
* PyCharm
* Git and GitHub

Example

Linear algebra problems can be represented and solved programmatically using Python.

import sympy as sp
A = sp.Matrix([
    [1, 2, 3],
    [2, 4, 7],
    [1, 1, 2]
])
rref_matrix, pivot_columns = A.rref()
print("RREF:")
print(rref_matrix)
print("Pivot columns:", pivot_columns)

This allows mathematical concepts such as pivots, rank, column space and null space to be explored computationally.

Why Linear Algebra?

Linear algebra provides much of the mathematical foundation for modern AI and machine learning. Vectors and matrices are used to represent and manipulate data, model transformations, and perform many of the computations underlying machine-learning systems.

Goals

As this repository develops, I plan to:

* Implement more advanced linear algebra concepts
* Strengthen my understanding through Python
* Explore applications to AI and machine learning
* Build small projects demonstrating practical uses of linear algebra
* Develop a portfolio combining mathematics and programming

Current Status

This repository is actively being developed as I expand my knowledge of linear algebra, Python, AI and machine learning.

