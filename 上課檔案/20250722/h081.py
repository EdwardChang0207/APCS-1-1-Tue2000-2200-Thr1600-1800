n,D=map(int,input().split())
a=list(map(int,input().split()))
m=0 #利潤
s=1 #有沒有股票
cost=a[0]
for i in range(1, n):
  if s==1 and a[i]>=cost+D:
    m += a[i]-cost
    s=0
    cost = a[i]
  elif s==0 and a[i]<=cost-D:
    s=1
    cost = a[i]
print(m)