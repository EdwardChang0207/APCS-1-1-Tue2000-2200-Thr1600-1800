n = int(input())
h = list(map(int,input().split()))
p = -1
path = 1
#重複掃描n個點
for i in range(0,n-1): 
#找一個起點h_i -> h_i+1... -> h_i+x >= h_i+x-1(路徑終止->設定新起點) -> path:x-1
    if h[i] > h[i+1]:
        path += 1
    else:
        if path > p: p = path
        path = 1
if path > p: p = path
print(p)