# 버블 정렬
import random

def bubble_sort(list):
    for i in range(0, len(list)-1):
        swap = False
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
                swap = True
        
        if swap == False:
            break
    
    print(list)

a = [random.randint(1, 100) for i in range(10)]
print(a)
bubble_sort(a)

li = [10, 2, 5, 3, 9, 12, 123, 3313, 23, 0, 23, 1, 42]

print(li)
bubble_sort(li)