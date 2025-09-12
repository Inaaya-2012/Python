list1 = [234,908,67,54]
list2 = [23,41,57,58]

sum = map(lambda x,y:x+y,list1,list2)
print(list(sum))

a = [4,789,21,35,78]
def square(x):
    return x**2

sq = map(square,a)

print("The square is",list(sq))