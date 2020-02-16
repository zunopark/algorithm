import sys

# 베르트랑 공준, 에레스테네스의 체를 통해 문제해결해야 함

# def sosu(n):
#     if n == 1:
#         return False
#     elif n == 2 or n == 3:
#         return True
#     else:
#         for i in range(2, n//2+1):
#             if n%i == 0:
#                 return False
#         return True

# def solution(n):
#     cnt = 0
#     for i in range(n+1, 2*n+1):
#         if sosu(i):
#             cnt += 1
#     print(cnt)
        

# while True:
#     temp = int(sys.stdin.readline().strip())
#     if temp == 0:
#         break
#     else:
#         solution(temp)