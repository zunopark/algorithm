n = int(input())

li = list(map(int, input().split()))

total = int(input())

def solution(num, li):
    res = 0
    for elem in li:
        if elem < num:
            res += elem
        else:
            res += num
    
    return res

start = 0
end = max(li)
mid = 0

while start<=end or solution(mid, li) > total:
    mid = (start + end) // 2

    check = solution(mid, li)

    if check <= total:
            start = mid + 1
    else:
        end = mid - 1
    
print(mid)