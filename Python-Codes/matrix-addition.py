order = int(input("enter order of matrices: "))

matrix1 = input("matrix 1 (for order = 2:1 2 3 4): ")
matrix2 = input("matrix 2 (for order = 2:5 6 7 8): ")

mat1 = [int(k) for k in matrix1.split()]
mat2 = [int(k) for k in matrix2.split()]



def matrix(mat1, mat2):
        if len(mat1) or len(mat2) != order*order:
                 print("wrong input, enter again")
                 matrix1 = input("matrix 1 (for order = 2:1 2 3 4): ")
                 matrix2 = input("matrix 2 (for order = 2:5 6 7 8): ")

                 mat1 = [int(k) for k in matrix1.split()]
                 mat2 = [int(k) for k in matrix2.split()]

                 result = []
                 for i in range(order * order):
                     result.append(mat1[i] + mat2[i])
                 print(result)


        else:
                result = []
                for i in range(order*order):
                    result.append(mat1[i] + mat2[i])
                print(result)

matrix(mat1, mat2)




