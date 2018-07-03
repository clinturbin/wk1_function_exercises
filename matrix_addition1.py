# matrix1 = [ [1, 3],
#             [2, 4] ]

# matrix2 = [ [5, 2],
#             [1, 0] ]

matrix1 = [ [2, 4],
            [5, 6] ]

matrix2 = [ [3, 7],
            [4, 2] ]

new_matrix = [ [],
               [] ]


for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        sum = matrix1[i][j] + matrix2[i][j]
        new_matrix[i].append(sum)


print new_matrix
