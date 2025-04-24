a = [1,2,3,5,6]
b = a[:]

b.insert(2,6)


print(max(a))
c = max(a)
print(a.index(c))
print(a)