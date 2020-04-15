n = int(input())

li = list()

for i in range(n):
    temp = list(map(int, input().split()))
    li.append(temp)

for i in range(len(li)):
    if li[i][1] - li[i][2] > li[i][0]:
        print('advertise')
    elif li[i][1] - li[i][2] == li[i][0]:
        print('does not matter')
    else:
        print('do not advertise')

