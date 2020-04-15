n,m = map(int, input().split())


def solution(result, check, m):
    if len(result) == m:
        for elem in result:
            print(elem, end=" ")
        print('')


        for i in range(m//2):
            result.pop()


        return


    for i in range(1, n+1):
        if check[i] == False:
            result.append(i)
            check[i] = True
            solution(result, check, m)
        else:
            continue



for i in range(1, n+1):
    check = [False] * (n+1)  # 현재 사용된 숫자 체크
    result = [] # 만들어진 숫자 보관
    result.append(i)
    check[i] = True
    solution(result, check, m)

