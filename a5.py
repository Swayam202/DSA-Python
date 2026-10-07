#Pallindrom ,arrys, string, funtion
num=int(input("Enter a number: "))
sum = 1
n=num
while (num>0):
    sum = sum*10 + (num%10)
    n = n//10
print(sum)