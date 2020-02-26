# 퀵 소트
import random

def quick_sort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[0]
    left = []
    right = []

    for i in range(1, len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

data_list = random.sample(range(100), 10)
print(data_list)
print(quick_sort(data_list))
