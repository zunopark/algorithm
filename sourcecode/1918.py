data = input()

stack=[]
prio = {'*':1, '/':1, '+':0, '-':0}


def check(elem):
    global stack
    global prio
    if len(stack) == 0 or stack[-1] == '(' or prio[elem] > prio[stack[-1]]:
        return True
    elif len(stack) != 0 or stack[-1] != '(' or prio[elem] <= prio[stack[-1]]:
        return False

for elem in data:
    if elem != '+' and elem != '-' and elem != '*' and elem != '/' and elem != '(' and elem != ')':
        print(elem, end="")
    elif elem == '(':
        stack.append(elem)
    elif elem ==')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            else:
                print(temp, end="")
    elif elem =='+' or elem =='-' or elem == '*' or elem == '/':
        if check(elem):
            stack.append(elem)
        else:
            while not check(elem):
                temp = stack.pop()
                print(temp, end="")
            stack.append(elem)

while stack:
    temp = stack.pop()
    print(temp, end="")
