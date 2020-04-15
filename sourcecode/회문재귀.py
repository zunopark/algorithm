def solution(data):
    if len(data) == 1:
        return True
    
    if data[0] == data[-1]:
        return True
    else:
        return False
    
    return solution([data[1:-1]])


while True:
    x = input()
    if x == 'q':
        break
    else:
        print(solution(x))

