## Kile Deal - 2013
## Project Euler Problem #16
## Status: Solved

import math

n = 2**1000
sum = 0

while n:
    digit = n % 10
    sum += digit
    n /= 10

print sum