#!/usr/bin/python3
# Author -Samow

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        j = 0
    else:
        j = 1
    print('{:s}'.format(chr(i - (j * 32))), end='')
