n = 12
mid=(n+1)//2

for i in range(n):
    for j in range(n):
        if (j==mid or i==mid):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()