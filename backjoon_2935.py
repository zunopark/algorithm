a = input()
b = input()
c = input()

if b == '+':
    if a>c:
        li = list(a)
        len_ = len(c)
        li[-len_] = '1'
        temp = "".join(li)
        print(temp)
    elif a==c:
        len_=len(a)-1
        print(2, end="")
        print('0'*len_, end="")
    else:
        li = list(c)
        len_ = len(a)
        li[-len_] = '1'
        temp = "".join(li)
        print(temp)
else:
    len_=len(a)+len(c)-2
    print(1, end="")
    print('0'*len_, end="")