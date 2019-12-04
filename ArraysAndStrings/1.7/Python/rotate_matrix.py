def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n//2):
        last = n - i - 1
        for j in range(i, last):
            offset = j - i
            print(matrix)
            top = matrix[i][j]
            matrix[i][j] = matrix[last-offset][i]
            matrix[last-offset][i] = matrix[last][last-j]
            matrix[last][last-j] = matrix[i+j][last]
            matrix[i+j][last] = top
    return matrix

if __name__=="__main__":
    n = int(input("Introduce length of array 'n'\n"))
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(int(input("Introduce Number\n")))
    rotated = rotate_matrix(matrix)
    print(rotated)

