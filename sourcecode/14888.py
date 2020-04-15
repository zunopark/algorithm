import itertools

n = int(input())
number = list(map(int, input().split()))
a,b,c,d = map(int, input().split())


li = []
for i in range(a):
    li.append('+')
for i in range(b):
    li.append('-')
for i in range(c):
    li.append('*')
for i in range(d):
    li.append('/')


case = list(map(''.join, itertools.permutations(li)))
case = set(case)
case = list(case)

result = []
again = number[:]

for elem in case:
    res = number.pop(0)
    for cal in elem:
        if cal == '+' and len(number) != 0:
            second = number.pop(0)
            res = res + second
        elif cal == '-' and len(number) != 0:
            second = number.pop(0)
            res = res - second
        elif cal == '*' and len(number) != 0:
            second = number.pop(0)
            res = res * second
        elif cal == '/' and len(number) != 0:
            second = number.pop(0)
            if res < 0:
                res = -res
                temp = res // second
                res = -temp
            else:
                res = res // second
                
    result.append(res)
    number = again[:]

print(max(result))
print(min(result))