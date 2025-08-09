a = int(input("Enter the Number 1:"))
b = int(input("Enter the Number 2:"))

choice = input("Enter the Choice (add/sub/mul/div/sqr):")

if (choice == 'add'):
    print("Answer is: ",a +b)
elif (choice == "sub"):
    print("Answer is: ",a - b)
elif (choice == "mul"):
    print("Answer is: ",a * b)
elif (choice == "div"):
    print("Answer is: ",a/b)
else:
    print("Answer is: ",a**b)