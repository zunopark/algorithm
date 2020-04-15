n,m = map(int, input().split())

li = list(map(int, input().split()))

start = 1
end = max(li)

while start<=end:
    mid = (start+end)//2

    res = 0
    for elem in li:
        if elem>= mid:
            res += elem - mid
    
    if res >= m:
        start = mid+1
    else:
        end = mid-1

print(end)
    