n = int(input())
s = [list(map(int,input().split())) for i in range(n)]
t = -1
s_max = -2
err = 0
for i in range(len(s)):
    if s[i][1] > s_max: #更新最高分
        s_max = s[i][1]
        t = s[i][0]
    if s[i][1] == -1: err += 1

#算總分
total = s_max - n - err * 2
if total < 0: total = 0
print(total,t)

# init -> 1 -> 2