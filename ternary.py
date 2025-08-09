"""
if(a>b):
    print("a is greater)
else:
    print("b is greater)
"""

a = 5
b = 6

print("a is greater" if (a>b) else 'b is Greater')

a = 4
b = 2
c = 5

print(("a is greater" if(a>c) else "c is greater") if (a>b) else ("b is greater" if(b>c) else "c is greater"))