def transpose_matrix(matrix):
    res = [[0 * i for i in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[j][i] = matrix[i][j]
    return res

