def perm(a):
    if len(a) > 1: 
        for i in range(len(a)):
            for j in perm(a[:i] + a[i+1:]):
                yield a[i] + j
    else: yield a

b = perm('0123456789')

for g in range(1000000-1):
    next(b)
print(next(b))

##2783915460
##Wall time: 2.75 s
