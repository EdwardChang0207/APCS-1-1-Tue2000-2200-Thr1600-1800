a1, b1, c1 = map(int,input().split())
a2, b2, c2 = map(int,input().split())
n = int(input())
r = []

def f(a,b,c,i):
    return a*i**2+b*i+c

for i in range(0, n+1):
    #計算 一號工廠給i個人的產值
    y1 = f(a1,b1,c1,i)
    #計算 二號工廠給n-i個人的產值
    y2 = f(a2,b2,c2,n-i)
    #total
    total = y1 + y2
    #記錄
    r.append(total)

print(max(r))