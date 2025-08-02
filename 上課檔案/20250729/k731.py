n=int(input())
# left=0
# right=0
# turn=0
# left, right, Uturn = 0, 0, 0
l, r, u = 0, 0, 0
v=[]

p=[list(map(int,input().split())) for _ in range(n)] #pn -> [xn,yn]
p.insert(0,[0,0])
for i in range(n):
  vi=[p[i+1][0]-p[i][0], p[i+1][1]-p[i][1]]
  v.append(vi)
for i in range(len(v)-1):
  x1, y1 = v[i]
  x2, y2 = v[i+1]
  V=x1*y2-x2*y1 #vi X vi+1 = vi.x * vi+1.y - vi.y * vi+1.x
  if V>0:
    l+=1
  elif V<0:
    r+=1
  else:
    if x1*x2 + y1*y2 < 0:
        u+=1
print(l,r,u)