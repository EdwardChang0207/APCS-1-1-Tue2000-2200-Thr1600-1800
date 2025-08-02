'''
l = [0]
if l: print(123)
else: print(456)
l = [i for i in range(10)]
print(l[0:3])
print(l[1::2])
l = []
for i in range(9):
    l.append(1)
l.insert(3, 8)
print(l)
item = l.pop(3)
print(l)
print(item)
l.remove(1)
print(l)
print(l.count(1))
print(l.index(1))
l = [i for i in range(9)]
l.reverse()
print(l)
l.sort()
print(l)
'''

l = [1, 2, 3, 4, 5, 6, 7]