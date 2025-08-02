n = int(input())
s = [list(map(int,input().split())) for _ in range(n)] #sn = [atk, dfn]

maximum, second = 0, -1 #位置
for i in range(1,len(s)):
    atk, dfn = s[i]
    if (atk**2 + dfn**2) > (s[maximum][0]**2 + s[maximum][1]**2):
        second = maximum
        maximum = i
    elif (atk**2 + dfn**2) > (s[second][0]**2 + s[second][1]**2):
        second = i
print(*s[second])