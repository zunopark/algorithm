n,m = map(int, input().split())

li=[]

for i in range(n):
    temp = input()
    temp = list(temp)
    li.append(temp)

# 리스트가 들어왔을때 최소 칠하는 값 리턴
def solution(li):
    cnt1 = 0
    cnt2 = 0

    if 1:
        for i in range(len(li)):
            for j in range(len(li[0])):
                if i%2==0:
                    if j%2==0:
                        if li[i][j] != 'W':
                            cnt1 += 1
                    else:
                        if li[i][j] != 'B':
                            cnt1 += 1
                else:
                    if j%2==0:
                        if li[i][j] != 'B':
                            cnt1 += 1
                    else:
                        if li[i][j] != 'W':
                            cnt1 += 1
    if 1:
        for i in range(len(li)):
            for j in range(len(li[0])):
                if i%2==0:
                    if j%2==0:
                        if li[i][j] != 'B':
                            cnt2 += 1
                    else:
                        if li[i][j] != 'W':
                            cnt2 += 1
                else:
                    if j%2==0:
                        if li[i][j] != 'W':
                            cnt2 += 1
                    else:
                        if li[i][j] != 'B':
                            cnt2 += 1 
    
    return min(cnt1, cnt2)


result = []

for i in range(0, n-7):
    temp = li[i:i+8]
    for j in range(0, m-7):
        res = []
        for elem in temp:
            a = elem[j:j+8]
            res.append(a)
        result.append(solution(res))

print(min(result))