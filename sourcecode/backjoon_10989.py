n = int(input())

# 수가 크니깐 배열에 담으면 메모리 초과가 발생한다.

li = [0]*10001

for i in range(n):
    temp = int(input())
    li[temp] += 1

for elem in li:
    if elem != 0:
        print(elem)