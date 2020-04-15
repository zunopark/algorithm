# insertion 정렬

import random

def select_sort(list):
    for i in range(0, len(list)-1):
        for j in range(len(list)-1, i, -1):
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]

    print(list)  


data_list = random.sample(range(100), 10)
print(data_list)
select_sort(data_list)

