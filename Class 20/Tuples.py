mtuple1 = (12,34.5,True,"RAJ")
print(mtuple1)

ituple = (12,34,56,77,33,33,23,33)
print(ituple)

print("The toatal no. of 33 in the tuple is",ituple.count(33))

mytuple = (100,2,300,89,7,56,12,3,45)

print("The element 3rd to 4th element in the tuple",mytuple[3:5])
print("The element all elements until 6th element",mytuple[:7])

mytuple =  mytuple + (1000,)
print(mytuple)