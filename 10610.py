n = list(input())

def check_three(num):
    if num % 3 == 0:
        return True
    else:
        return False

def check_ten(list):
    if '0' in list:
        return True
    else:
        return False

check_3 = 0
#check_10 = int("".join(n))

for elem in n:
    check_3 += int(elem)

if check_three(check_3) and check_ten(n):
    n.sort(reverse=True)
    print("".join(n))
else:
    print(-1)



