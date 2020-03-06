# 그리디 알고리즘


n = int(input())
li = list(map(int, input().split()))
li.sort()
sum = 0

for i in range(n):
    temp = 0
    for j in range(i+1):
        temp += li[j]
    sum += temp

print(sum)


