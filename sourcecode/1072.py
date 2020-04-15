import math
import sys

x,y = map(int, input().split())

def get(x,y, plus):
    return math.floor((y+plus)/(x+plus)*100)

start = 0
end = 1000000000
check = get(x,y,0)

if check == 99 or check == 100:
    print(-1)
    sys.exit()

while start<=end:
    mid = (start+end) // 2

    if get(x,y,mid) >= check:
        end = mid - 1
    else:
        start = mid + 1

print(mid)
        
