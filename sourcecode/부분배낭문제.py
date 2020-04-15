import sys

data_list = [(10,10), (15,12), (20,10), (25,8), (30,5)]

capacity = 30

def solution(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0

    for elem in data_list:
        if capacity-elem[0]>=0:
            total_value += elem[1]
            capacity -= elem[0]
        else:
            fraction = capacity / elem[0]
            total_value += fraction * elem[1]
            break
    
    return total_value

print(solution(data_list, capacity))
