n = input()
A = sum([int(i) for i in n[::2]])
B = sum([int(i) for i in n[1::2]])
print(abs(A-B))