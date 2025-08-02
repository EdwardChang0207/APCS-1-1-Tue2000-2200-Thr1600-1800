n = int(input())
h = list(map(int,input().split()))
cost = 0

for i in range(len(h)):
    if h[i] == 0:
        #比較左右長度取min
        if i == 0:
            cost += h[i+1]
        elif i == len(h)-1:
            cost += h[i-1]
        else:   
            cost += min(h[i-1], h[i+1])

print(cost)