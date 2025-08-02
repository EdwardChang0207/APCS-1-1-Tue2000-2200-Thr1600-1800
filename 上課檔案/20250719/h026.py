F = input()
N = int(input())
y = input().split()

last = -1
game = False
round = 1
# 字典
win = {'0':'2', '2':'5', '5':'0'}
lose = {'2':'0', '5':'2', '0':'5'}
record = [F]
for i in y:
    #判斷輸贏
    #(1)分出勝負
    if win[F] == i: #哥哥贏
        print(*record, f': Won at round {round}')
        game = True
        break
    elif lose[F] == i: #哥哥輸
        print(*record, f': Lost at round {round}')
        game = True
        break
    elif round == N: break
    #(2)平手
    if i == last:#絲絲兩輪出一樣的
        if i == '0': F = '5'
        elif i == '2': F = '0'
        else: F = '2'
    else:
        F = i
    last = i
    round += 1
    record.append(F)

if not game:
    print(*record, f': Drew at round {N}')
