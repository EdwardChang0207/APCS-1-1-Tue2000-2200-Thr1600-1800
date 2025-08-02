a, b = map(int,input().split())
n = int(input())
t = list(map(int,input().split()))
r = 0
#重複n個人
for i in t:
    #到達終點是紅or綠燈
    #if 是紅燈:計算等待的秒數 -> w
    if i % (a+b) >= a: #等紅燈
        w = (a+b) - i % (a+b)
        r += w
print(r)