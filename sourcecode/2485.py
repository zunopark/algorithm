n = int(input())

tree = []

def check(li):
    a = li[1] - li[0]
    for i in range(2, len(li)):
        if li[i]-li[i-1] != a:
            return False

    return True
    
def solution(r):
    start = min(tree)
    end = max(tree)
    cnt = 0
    check = True
    idx = 1

    while start<end:
        start = start + r
        if start > tree[idx]:
            check = False
            break
        elif start == tree[idx]:
            check = True
            if idx + 1 < len(tree):
                idx += 1
            else:
                idx = len(tree)-1
        elif start < tree[idx]:
            cnt += 1
            if start + r < tree[idx]:
                check = True
            else:
                if idx + 1 < len(tree):
                    idx += 1
                else:
                    idx = len(tree)-1
    
    if check:
        return cnt
    else:
        return 100001



for i in range(n):
    tree.append(int(input()))


if check(tree):
    print(0)
    
max_range = (max(tree) - min(tree)) // (len(tree) - 1)

result = 100000
for i in range(1, max_range+1):
    temp = solution(i)
    if temp < result:
         result = temp
    
print(result)






