import sys

print_list = []


def dfs(start):
    if len(print_list) == 6:
        for elem in print_list:
            print(elem, end=" ")
            return

    print_list.append(temp[start])
    dfs(start+1)



while True:
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == 0:
        break
    temp.pop(0)

    dfs(0)

