matrix1 = [ [2, 4],
            [5, 6] ]

matrix2 = [ [3, 7],
            [4, 2] ]

new_matrix = [ [0, 0],
               [0, 0] ]


for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        for k in range(len(matrix1)):
            new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

print new_matrix


# Use function for above



