## Kile Deal - 2013
## Project Euler Problem #29
## Status: Solved

from itertools import permutations

n = range(2, 101)

comb_powers = [x[0]**x[1] for x in permutations(n, 2)]

i_powers = [i**i for i in n]

c_set = set(comb_powers)
i_set = set(i_powers)

print( len(c_set | i_set) )
