num = int(input())
data = input()

stack=[]
number=[]

for i in range(num):
    number.append(int(input()))

idx = 0

for elem in data:
    if elem != '+' and elem != '-' and elem != '*' and elem != '/':
        stack.append(number[idx])
        idx += 1
    else:
        b = stack.pop()
        a = stack.pop()
        if elem == '+':
            stack.append(a+b)
        elif elem == '-':
            stack.append(a-b)
        elif elem == '*':
            stack.append(a*b)
        elif elem == '/':
            stack.append(a/b)

print(round(stack[0], 2))