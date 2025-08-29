list1 = [45,67,91,53,28,11,23]

sum = 0
for i in list1:
    sum+=i

avg = sum / len(list1)
print("The sum is",sum)
print("The average is",avg)

print("The maximum element is",max(list1))
print("The minimum element is",min(list1))