"""def rotate_matrix(matrix):
    n = len(matrix)
    shifted = []
    for i in range(n):
        shifted.append([])
        for j in range(n):
            shifted[i].append(matrix[j][n-1-i])
    return shifted
matrix = [[0,1,2,3],
         [4,5,6,7],
         [8,9,0,1], 
         [2,3,4,5]]
print(rotate_matrix(matrix))"""
def rotate_matrix(matrix):
    n = len(matrix)
    pass