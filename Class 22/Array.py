import array as arr
a = arr.array('i',[12,67,90,57,21])
print("The aaray given is\n",str(float))

floatar = arr.array('d',[12.44,56.9,90.23,987.77,12.334])
print("The array given is \n",str(floatar))

print("The count of 23 in array a is",a.count(23))

a.append(1000)
print("The array after appending 1000 \n",str(a))

a.reverse()
print("The reverse of the array is \n",str(a))