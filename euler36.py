## Kile Deal - 2013
## Project Euler Problem #36
## Status: Solved

p = list()

for n in xrange(10**6):
    if str(n) == str(n)[::-1] and str(bin(n))[2:] == (str(bin(n))[2:])[::-1]:
        p.append(n)
        
print sum(p)