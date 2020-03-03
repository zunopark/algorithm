import sys

x,y = map(int, sys.stdin.readline().split())

day = ['MON','TUE','WED', 'THU', 'FRI', 'SAT', 'SUN']

sum_day = y

if x == 1:
    sum_day -= 1
elif x == 2:
    sum_day += 31
    sum_day -= 1
elif x == 3:
    sum_day += 59
    sum_day -= 1
elif x == 4:
    sum_day += 90
    sum_day -= 1
elif x == 5:
    sum_day += 120
    sum_day -= 1
elif x == 6:
    sum_day += 151
    sum_day -= 1
elif x == 7:
    sum_day += 181
    sum_day -= 1
elif x == 8:
    sum_day += 212
    sum_day -= 1
elif x == 9:
    sum_day += 243
    sum_day -= 1
elif x == 10:
    sum_day += 273
    sum_day -= 1
elif x == 11:
    sum_day += 304
    sum_day -= 1
elif x == 12:
    sum_day += 334
    sum_day -= 1

print(day[sum_day%7])
