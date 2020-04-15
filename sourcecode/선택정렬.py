# 선택 정렬

import random

def select_sort(list):
    for i in range(0, len(list)-1, 1):
        _min = list[i]
        idx = i
        for j in range(i+1, len(list), 1):
            if list[j] < _min:
                _min = list[j]
                idx = j
        list[i], list[idx] = list[idx], list[i]
    
    print(list)

data_list = random.sample(range(100), 10)
print(data_list)
select_sort(data_list)
