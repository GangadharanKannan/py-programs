set1 = {1,2,3,4,5}
set2 = {2,3,4,5,6,8,9}

set1.add(7)
set2.remove(9)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))