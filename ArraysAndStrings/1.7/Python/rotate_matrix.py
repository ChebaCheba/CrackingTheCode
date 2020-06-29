def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n//2):
        last = n - i - 1
        for j in range(i, last):
            offset = j - i
            top = matrix[i][j]
            matrix[i][j] = matrix[last-offset][i]
            matrix[last-offset][i] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i+offset][last]
            matrix[i+offset][last] = top
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

