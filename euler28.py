## Kile Deal - 2013
## Project Euler Problem #28
## Status: Solved

total = 0

x = 1
increment = 2
ct = 0


while x <= 1001**2:
    total += x
    x += increment
    ct += 1
    if ct == 4:
        ct = 0
        increment +=2
    
print total
