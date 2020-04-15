import sys

n = int(input())
li = []
for i in range(n):
    temp = list(input())
    li.append(temp)

result = 0

def check(li):
    result1 = 1
    result2 = 1

    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            result1 += 1
    
    for i in range(len(li)-1, 0, -1):
        if li[i] == li[i-1]:
            result2 += 1

    return max(result1, result2)

def solution(li):
    row_result = 0
    col_result = 0

    for i in range(0, len(li)):
        temp = li[i]
        if check(temp)>row_result:
            row_result = check(temp)
    
    
    for i in range(0, len(li)):
        temp_list = []
        for j in range(0, len(li)):
            temp_list.append(li[j][i])
        if check(temp_list) > col_result:
            col_result = check(temp_list)
    
    return max(row_result, col_result)
    


for i in range(0, len(li)):
    temp = li[i]
    for j in range(0, len(li)-1):
        if temp[j] != temp[j+1]:
            temp[j], temp[j+1] = temp[j+1], temp[j]

            if solution(li)>result:
                result = solution(li)
            
            temp[j], temp[j+1] = temp[j+1], temp[j]

for i in range(0, len(li)-1):
    temp1 = li[i]
    temp2 = li[i+1]
    for j in range(0, len(li)):
        if temp1[j] != temp2[j]:
            temp1[j], temp2[j] = temp1[j], temp2[j]

            if solution(li)>result:
                result = solution(li)
            
            temp1[j], temp2[j] = temp1[j], temp2[j]
        
            
print(result)