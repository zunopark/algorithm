import sys
import itertools

n = int(input())
matrix=[]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    matrix.append(temp)


num_list = [i for i in range(n)]
result = sys.maxsize - 1

def solution():
    global result

    for cand in itertools.combinations(num_list, n//2):
        start = list(cand)
        link = list(set(num_list)-set(cand))

        start_comb = list(itertools.combinations(start, 2))
        link_comb = list(itertools.combinations(link, 2))

        start_sum = 0
        for x,y in start_comb:
            start_sum += (matrix[x][y]+matrix[y][x])
        
        link_sum = 0
        for x,y in link_comb:
            link_sum += (matrix[x][y]+matrix[y][x])
        
        check = abs(start_sum-link_sum)
        if check < result:
            result = check

solution()
print(result)
