n,m = map(int, input().split())
cases = list(map(int, input().split()))

def check(length):
    result = 0
    count = 1

    for elem in cases:
        if elem > length:
            return False
        
        result += elem
        if result > length:
            result = elem
            count += 1
        
    return m >= count


start = 1
end = sum(cases)
result = 0

while start<=end:
    mid = (start+end) // 2

    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)





