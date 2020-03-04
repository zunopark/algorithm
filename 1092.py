import sys

n = int(input()) # 크레인 개수
crain = list(map(int, input().split()))

m = int(input()) # 박스의 개수
box = list(map(int, input().split()))


cnt = 0
result = 0
box.sort(reverse=True)
crain.sort(reverse=True)
pos = [0] * n
check = [False] * m

if box[0] > crain[0]:
    print(-1)
    sys.exit(1)
else:
    while True:
        if cnt == len(box):
            break
        else:
            for i in range(n):
                while pos[i] < len(box):
                    if not check[pos[i]] and crain[pos[i]]>=box[pos[i]]:
                        check[pos[i]] = True
                        pos[i] += 1
                        cnt += 1
                        break
                    pos[i] += 1
            result += 1

print(result)


