## Kile Deal - 2013
## Project Euler Problem #24
## Status: Solved

from itertools import permutations

x = '0123456789'
n = list(map("".join, permutations(x)))
print n[999999]