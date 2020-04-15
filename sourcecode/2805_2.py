n,m = map(int, input().split())

tree = list(map(int, input().split()))

def get(height):
    temp = 0
    for elem in tree:
        if elem <= height:
            continue
        else:
            temp += elem - height
    
    return temp

start = 0
end = max(tree)

while start<=end:
    mid = (start + end) // 2

    if get(mid) >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)