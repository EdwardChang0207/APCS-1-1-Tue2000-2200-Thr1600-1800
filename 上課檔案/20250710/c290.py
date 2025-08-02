n = input()
A, B = 0, 0
for i in range(len(n)):
    if i % 2 == 0: #奇位數
        A += int(n[i])
    else:#偶位數
        B += int(n[i])

# if A-B < 0: print(-1*(A-B))
# else:print(A-B)

print(abs(A-B))