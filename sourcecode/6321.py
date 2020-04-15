import sys

n = int(input())

alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(n):
    temp = input()
    print('String #', end="")
    print(i+1)
    for elem in temp:
        idx = alp.index(elem)
        if idx == len(alp)-1:
            idx = 0
        else:
            idx += 1
        print(alp[idx], end="")
    print('')