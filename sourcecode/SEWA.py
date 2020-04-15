cnt = 0

def is_palin(li):
    for i in range(0, len(li)//2, 1):
        if li[i] != li[-1-i]:
            return False
    return True


def row_check(matrix, length):
    global cnt
    for j in range(0, 8, 1):
        temp = matrix[j]
        for i in range(0, 9-length, 1):
            check = temp[i:i+length]
            if is_palin(check):
                cnt += 1

def col_check(matrix, length):
    global cnt
    for i in range(0, 8, 1):
        for j in range(0, 9-length, 1):
            temp = []
            for k in range(j, j+length, 1):
                temp.append(matrix[k][i])
            
            if is_palin(temp):
                cnt += 1


for i in range(10):
    cnt = 0
    matrix = []
    num = int(input())
    for j in range(8):
        temp = list(input())
        matrix.append(temp)
    
    row_check(matrix, num)
    col_check(matrix, num)

    print('#', end="")
    print(i+1, end=" ")
    print(cnt)

    
    
