import sys


li = []

for i in range(5):
    li.append(int(sys.stdin.readline().strip()))

hamburger = li[:3]
drink = li[3:]

print(min(hamburger)+min(drink)-50)