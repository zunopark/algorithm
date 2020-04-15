import sys
import itertools


while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break
    k = temp.pop(0)
    for elem in list(itertools.combinations(temp, 6)):
        for i in elem:
            print(i, end=" ")
        print('')
        
    print('')