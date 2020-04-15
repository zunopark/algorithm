n = int(input())
cases = list(map(int, input().split()))
m = int(input())

def get(height):
    temp = 0
    for elem in cases:
        if elem < height:
            temp += elem
        else:
            temp += height
    
    return temp


start = 0
end = 100000
mid = 0

while start<=end or get(mid) > m:
    mid = (start+end) // 2

    if get(mid) > m:
        end = mid - 1
    else:
        start = mid + 1

print(mid)