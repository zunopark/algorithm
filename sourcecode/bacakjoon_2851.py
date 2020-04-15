import sys

def solution(number):
    return abs(100-number)


li = [int(sys.stdin.readline().strip()) for i in range(10)]

current = li[0]
prev = li[0]

for i in range(1, len(li)):
    current += li[i]
    if solution(current) < solution(prev):
        prev = current
    elif solution(current) == solution(prev):
        prev = max(current, prev)

print(prev)
