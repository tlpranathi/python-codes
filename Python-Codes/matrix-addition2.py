# Python function that takes 2D matrices (list of lists) as input and returns their sum
def add_matrices(matrix1, matrix2):
    result = [[0 for k in range(len(matrix1[0]))] for k in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# example
matrix1 = [[1,1,1,2],[1,1,1,2],[1,1,1,2],[1,1,1,2]]
matrix2 = [[1,1,1,2],[1,1,1,2],[1,1,1,2],[1,1,1,2]]

result = add_matrices(matrix1, matrix2)

for row in result:
    print(row)