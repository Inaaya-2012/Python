a = ['a','b','c']
b = [1,2,3]

zip1 = list(zip(a,b))
print(zip1)

a1 = [10,20,30,40]
a2 = [1000,2000,3000,4000]

for (x,y)in zip(a,a2[::-1]):
    print(x,y)

stocks = ['reliaince','infoysys','TCS']
prices = [213,324,34]

new_dict = {s:p for s,p in zip(stocks,prices)}
print(new_dict)