n = int(input("Enter the Num :"))

for j in range(1, n+1):
    for i in range(1, j+1):
        print(i, end=" ")
    print()


for j in range(1, n+1):
    for i in range(1, j+1):
        print("*", end=" ")
    print()