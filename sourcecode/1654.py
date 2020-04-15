n,k = map(int, input().split())

li=[]

for i in range(n):
    li.append(int(input()))

start = 1
end = max(li)


while True:
    if start > end:
        break

    mid = (start+end)//2
    res = 0
    for elem in li:
        res += elem // mid
        
    if res >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)