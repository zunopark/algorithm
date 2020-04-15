# import sys

# n = int(input())
# li = list(map(int, sys.stdin.readline().split()))

# res = []

# for i in range(0, len(li)-1):
#     _max = li[i]
#     for j in range(i+1, len(li)):
#         if _max + li[j] > _max:
#             _max += li[j]
#         else:
#             break
#     res.append(_max)

# print(max(res))

n = int(input())
num_list = list(map(int, input().split()))
temp = [0 for _ in range(n)]
result = -1001

for i in range(n):
    temp[i] = max(temp[i-1] + num_list[i], num_list[i])
    result = max(result, temp[i])
        
print(result)