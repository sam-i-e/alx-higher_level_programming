#!/usr/bin/python3
# Author - Samow

i = 0
while i < 8:
    j = i
    while j <= 9:
        if i != j:
            print('{}{}'.format(i, j), end=', ')
        j += 1
    i += 1
print('{}{}'.format(i, j - 1), sep='')
