def solution(x,y):
    if y < 2:
        return x
    else:
        return x * solution(x, y-1)

for i in range(10):
    n = int(input())
    x,y = map(int, input().split())
    print('#', end="")
    print(n, end=" ")
    print(solution(x,y))