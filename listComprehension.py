lst = [1,2,3,4,5,6,7,8,9]

even = [i for i in lst if i%2 == 0]
odd = [i for i in lst if i%2 == 1]

print(even, odd, sep='\n')