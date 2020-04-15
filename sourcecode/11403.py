import sys

N = int(sys.stdin.readline().strip())

matrix = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    matrix.append(temp)




for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1

for elem in matrix:
    for i in elem:
        print(i, end=" ")
    print('')
