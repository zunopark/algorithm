n = int(input())
m = int(input())
s = input()

def make(n):
    if n == 1:
        return 'IOI'
    else:
        temp = 'IOI'
        for i in range(1, n):
            temp += 'OI'
        return temp


check = make(n)
cnt = 0
length = m-len(check)+1

for i in range(length):
    temp = s[i:i+len(check)]
    if temp == check:
        cnt += 1

print(cnt)