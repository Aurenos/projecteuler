## Kile Deal - 2013
## Project Euler Problem #30
## Status: Solved

pfifths = [i**5 for i in xrange(10)]
nums = list()
n = 2

while n < 2*sum(pfifths):
    strnum = str(n)
    digits = [int(i) for i in strnum]
    digit_fifths = [j**5 for j in digits]
    if sum(digit_fifths) == n:
        nums.append(n)
    n += 1
    
print nums
print sum(nums)