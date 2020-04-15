def get_check(a, b):
    li = [a, b]
    li.sort()
    if li.index(a) < li.index(b):
        return True
    else:
        return False

def sort_as_dict(list):
    for i in range(len(list)-1):
        if len(list[i]) == len(list[i+1]):
            if get_check(list[i], list[i+1]):
                continue
            else:
                list[i], list[i+1] = list[i+1], list[i]
        else:
            continue

def sol(list):
    final = []
    for i in range(0, len(list)-1):
        li = []
        if len(list[i]) == len(list[i+1]):
            while len(list[i]) == len(list[i+1]):
                li.append(list[i])
                i += 1
            li.sort()
            final.append(li)
        else:
            final.append(list[i])
    
    return final
        



n = int(input())
li = []

for i in range(n):
    temp = input()
    li.append(temp)

for i in range(1, n):
    for j in range(0, i+1):
        if len(li[j]) > len(li[i]):
            li[j], li[i] = li[i], li[j]


print(sol(li))