def solution(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    
    return solution(num-1) + solution(num-2) + solution(num-3)

t_case = int(input())

li = []

for i in range(t_case):
    li.append(int(input()))

for elem in li:
    print(solution(elem))