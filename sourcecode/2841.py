n, p = map(int, input().split())

queue = [[] for i in range(6)]

cnt = 0

for i in range(n):
    line, pret = map(int, input().split())

    if len(queue[line-1]) == 0:
        queue[line-1].append(pret)
        cnt += 1
    else:
        if queue[line-1][-1] < pret:
            queue[line-1].append(pret)
            cnt += 1
        elif queue[line-1][-1] == pret:
            pass
        elif queue[line-1][-1] > pret:
            temp = 0
            while queue[line-1]:
                if queue[line-1][-1] > pret:
                    temp = queue[line-1].pop()
                    cnt += 1
                else:
                    break

            if temp != pret:
                queue[line-1].append(pret)
                cnt += 1

print(cnt)
