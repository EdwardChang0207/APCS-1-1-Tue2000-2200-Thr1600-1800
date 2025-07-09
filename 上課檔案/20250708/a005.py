t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    if a[1]-a[0] == a[2]-a[1]: #等差
        b = a[3] + a[1] - a[0]
    else:#等比
        b = a[3] * (a[1] // a[0])
    print(*a,b)#* for all -> print(a[0],a[1],a[2],a[3])