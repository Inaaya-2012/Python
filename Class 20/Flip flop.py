def flipflop(r):
    s =  0
    e = len(r) - 1
    while s < e:
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True

r = (1,2,3,3,2,10)
if flipflop(r):
    print("The given tuple is flipflop")
else:
    print("The given tuple is not a flipflop")        