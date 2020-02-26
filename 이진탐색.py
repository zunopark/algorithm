import sys
import random


a = [1,2,3,4,5,6,7,8,9,10]

def binary_search(list, value):
    if len(list) == 1 and list[0] == value:
        return True
    if len(list) == 1 and list[0] != value:
        return False
    if len(list) == 0:
        return False
    
    mid = len(list) // 2
    if value == list[mid]:
        return list[mid]
    else:
        if value < list[mid]:
            return binary_search(list[:mid], value)
        else:
            return binary_search(list[mid:], value)

print(binary_search(a, 3))