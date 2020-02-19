l = int(input()) # 날짜
a = int(input()) # 국어
b = int(input()) # 수학
c = int(input()) # 국어하루최대
d = int(input()) # 수학하루최대

while True:
    l -= 1
    a -= c
    b -= d
    if a <= 0 and b <= 0:
        break

print(l)

