def set_to_zero(matrix):
    row = set()
    column = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 0):
                if (i not in row):
                    row.add(i)
                if (j not in column):
                    column.add(j)
            else: 
                if (i in row) or (j in column):
                    matrix[i][j] = 0
        j = 0
        if i in row:
            while matrix[i][j] != 0:
                matrix[i][j] = 0
                j += 1

    return matrix

if __name__=="__main__":
    n = int(input("Number of rows\n"))
    m = int(input("Number of columns\n"))
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            number = int(input("Introduce Number\n"))
            matrix[i].append(number)
    print(set_to_zero(matrix))