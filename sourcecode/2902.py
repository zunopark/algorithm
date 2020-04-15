data = input()

res = []

res.append(data[0])

for i in range(1, len(data)):
    if data[i] == '-':
        res.append(data[i+1])

print("".join(res))