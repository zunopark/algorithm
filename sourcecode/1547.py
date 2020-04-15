n = int(input())

li = [1,2,3]
res = []

def swap(li, list):
    a = list[0] # 3
    b = list[1] # 1

    idx1 = li.index(a) # 2
    idx2 = li.index(b) # 0

    li[idx1], li[idx2] = li[idx2], li[idx1]



for i in range(n):
    temp = list(map(int, input().split()))
    res.append(temp)

for elem in res:
    swap(li, elem)

print(li[0])

