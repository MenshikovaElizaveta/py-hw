from my_matrix_package import Matrix


A = Matrix(2, 2, [[1, 2], [3, 4]])
B = Matrix(2, 2, [[5, 6], [7, 8]])

print("Матрица A:")
print(A.data)

D = A.__nummul__(3) 
print("\nA * 3:")
print(D.data)
