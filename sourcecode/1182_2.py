import itertools

n,s = map(int, input().split())
li = list(map(int, input().split()))

num = len(li)
result = 0


def make(li, num):
    return list(itertools.combinations(li, num))


while num > 0:
    cases = make(li, num)

    for elem in cases:
        if sum(elem) == s:
            result += 1

    num -= 1


print(result)