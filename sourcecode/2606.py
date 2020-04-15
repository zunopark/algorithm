import sys

num = int(input())

def dfs(v, matrix, answer):
    for i in matrix[v]:
        if i not in answer:
            answer.append(i)
            dfs(i, matrix, answer)
    
    return answer


matrix = [[] for i in range(num+1)]

m = int(input())

for i in range(1, m+1):
    a,b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

print(len(dfs(1, matrix, [1]))-1)