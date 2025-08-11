#palindrome checker

a = input("Enter the Palindrome :")

if a == a[::-1]:
    print("It is a Palindrome")
else:
    print("it is not Palindrome")