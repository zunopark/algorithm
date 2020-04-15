n = int(input())
data = input()

alp = [0, 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

res = 0

for i in range(n):
    temp = alp.index(data[i])
    res += temp * 31**(i)

print(res%1234567891)