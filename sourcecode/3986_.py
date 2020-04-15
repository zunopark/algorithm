n = int(input())
cnt = 0

def solution(word):
    stack = []

    for elem in word:
        if not stack:
            stack.append(elem)
        else:
            if stack[-1] == elem:
                stack.pop()
            else:
                stack.append(elem)
    
    if len(stack) == 0:
        return True
    else:
        return False


for i in range(n):
    temp = input()
    if solution(temp):
        cnt += 1

print(cnt)

