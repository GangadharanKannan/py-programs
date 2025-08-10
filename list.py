lst = [1, 2, 3, 4, 5, 6]
lst2 = [7, 8 ,9]

print(lst[2])
lst.append(8)
lst.insert(1, 20) 

lst.pop()
lst.extend(lst2)
lst.remove(9)

print(len(lst))

print(lst[1:4])

print(lst)