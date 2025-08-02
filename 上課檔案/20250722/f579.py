a, b = map(int, input().split())
n = int(input())
carts = [list(map(int, input().split())) for _ in range(n)]
r = 0
for cart in carts:
    #檢查一台
    cart.sort()
    for item in cart:
    #把移除的商品刪去
        if item >= 0: break
        cart.remove(-item)
    #判斷 a,b是否同時存在 -> 記錄(r+=1)
    if (a in cart) and (b in cart): r += 1
print(r)
