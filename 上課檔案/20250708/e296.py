r = 0
#重複兩次
for i in range(2):
    #處理一場比賽
    #(1)拿分數 (2)加總 (3)輸出比數 (4)記錄
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f'{sum(a)}:{sum(b)}')
    if sum(a) > sum(b): r += 1
    else: r -= 1

if ...: print('Win')
elif ...: print('Tie')
else: print('Lose')