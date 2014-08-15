## Kile Deal
## Euler Problem #55

def is_lychrel(x):
    result = x
    for _ in xrange(51):
        result = result + int(str(result)[::-1])
        if int(str(result)) == int(str(result)[::-1]):
            return False
    
    return True

lychrel_ct = 0
    
for i in xrange(10000):
    lychrel_ct += 1 if is_lychrel(i) else 0
    
print lychrel_ct