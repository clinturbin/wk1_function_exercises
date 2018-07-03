# matrix1 = [ [2, 4, 5], [1, 2, 3], [1, 2, 3] ]

# matrix2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

# matrix1 = [ [1, 2, 3, 4], [1, 2], [1, 2, 3], [1, 2, 3, 4] ]
# matrix2 = [ [3, 4, 5, 6], [5, 6], [5, 6, 7], [5, 6, 7, 8] ]

# new_matrix = []


# for i in range(len(matrix1)):
#     new_matrix.append([])
#     for j in range(len(matrix1[i])):
#         sum = matrix1[i][j] + matrix2[i][j]
#         new_matrix[i].append(sum)
        
# print new_matrix


# note: below is the code we did in class

# REDO MATRIX ADDITION WITH FUNCTIONS

def create_empty_matrix(width, height):
    result = []
    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(0)
    return result

def add_matrixes(m1, m2):
    height = len(m1)
    width = len(m1[0])
    matrix = create_empty_matrix(width, height)
    for i in range(0, height):
        for j in range(0, width):
            cell1 = m1[i][j]
            cell2 = m2[i][j]
            matrix[i][j] = cell1 + cell2
    return matrix

matrix1 = [ [2, 4],
       [5, 6] ]

matrix2 = [ [3, 7],
       [4, 2] ]

result = add_matrixes(matrix1, matrix2)

print result