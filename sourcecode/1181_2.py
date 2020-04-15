n = int(input())

dict = {}

for i in range(n):
    temp = input()
    length = len(temp)
    dict[temp] = length

result = []

for k,v in dict.items():
    result.append([k,v])

result.sort()
result.sort(key = lambda x : x[1])

for elem in result:
    print(elem[0])