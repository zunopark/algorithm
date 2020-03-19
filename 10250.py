import sys

t = int(input())

while t:
    h,w,n = map(int, input().split())
    li = []
    start = 101

    for i in range(w):
        temp = [i for i in range(start, start*h+1, 100)]
        li.append(temp)
        start += 1

    cnt = 1

    for i in range(w):
        for j in range(h):
            if cnt == n:
                print(li[i][j])
            cnt += 1
    t -= 1


