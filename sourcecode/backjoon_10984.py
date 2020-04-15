t = int(input())


def solution(li):
    cnt = 0
    gpa = 0
    for elem in li:
        cnt += elem[0]
        gpa += elem[0] * elem[1]
    print(int(cnt), round(gpa/cnt, 1))


for i in range(t):
    n = int(input())
    li = list()
    for j in range(n):
        temp = list(map(float, input().split()))
        li.append(temp)
    solution(li)
