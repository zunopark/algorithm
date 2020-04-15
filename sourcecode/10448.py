t = int(input())

def generate(number):
    return number*(number+1) // 2

li = []
idx = 1
while True:
    temp = generate(idx)
    if temp>1000:
        break
    else:
        li.append(temp)
    
    idx += 1

def solution(data):
    for i in range(0, len(li)):
        for j in range(0, len(li)):
            for k in range(0, len(li)):
                if li[i] + li[j] + li[k] == data:
                    print(1)
                    return
                    
    print(0)
    

for i in range(t):
    a = int(input())
    solution(a)
