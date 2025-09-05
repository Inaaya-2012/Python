dic1 = {'coding':2,'my':3,'school':2,'bag':1,'pen':2}
print(str(dic1))
k = 2
count = 0 
for key in dic1.keys():
    if dic1[key] == k:
        count+= 1

print(f"The words which has {k} frequency is {count}")        