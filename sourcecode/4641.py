import sys

while True:
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == -1:
        break

    temp.sort()
    cnt = 0
    for i in range(0, len(temp)-1):
        for j in range(i+1, len(temp)):
            if temp[j] == temp[i] * 2:
                cnt += 1
    
    print(cnt)