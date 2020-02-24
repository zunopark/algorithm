n = int(input())

count = 0

def solution(num):
    if num == 1:
        return num
    global count
    if num % 3 == 0:
        count += 1
        return solution(num//3)
    elif num % 2 == 0:
        count += 1
        return solution(num//2)
    else:
        count += 1
        return solution(num-1)

solution(n)
print(count)


        


    