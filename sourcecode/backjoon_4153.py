def check(data):
    if int(data[0])**2 + int(data[1])**2 == int(data[2])**2 or int(data[0])**2 + int(data[2])**2 == int(data[1])**2 or int(data[1])**2 + int(data[2])**2 == int(data[0])**2:
        return True
    else:
        return False 


li = []

while True:
    temp = input().split()
    if temp.count('0') == 3:
        break
    else:
        li.append(temp)

for elem in li:
    if check(elem):
        print('right')
    else:
        print('wrong')