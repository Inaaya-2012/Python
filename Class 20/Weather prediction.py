w = (1,0,0,0,1,1,0,1,1)

s = w.count(0)
r = w.count(1)

if s >= r:
    print("The weather is good")
else:
    print("The weather is not good")    