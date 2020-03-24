data = list(input())
bomb = input()

answer = []
length = len(bomb)

for i in range(len(data)):
    answer.append(data[i])
    if data[i] == bomb[-1]:
        check = True
        for j in range(0, length):
            if bomb[j] != answer[-1-length+1+j]:
                check = False
        
        if check:
            for k in range(length):
                answer.pop()

if len(answer) == 0:
    print('FRULA')
else:
    print("".join(answer))
