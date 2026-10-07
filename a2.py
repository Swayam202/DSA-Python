n = int(input("Enter the numbers: "))
rev = 0

while n:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)