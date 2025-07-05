# percentage calculation

print("Enter the marks you got in all 4 subjects:")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math+english+science+hindi
print("The sum of the marks of math,english,science and hindi is",sum,end =" " )
perc = (sum/400)*100

print( "Percentage Mark = ",perc)

