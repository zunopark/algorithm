import sys

n = int(sys.stdin.readline().strip())


result = {}
for i in range(n):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        result[name] = True
    else:
        del result[name]

print("\n".join(sorted(result.keys(), reverse=True)))