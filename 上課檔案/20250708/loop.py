#while -> 不知跑幾次
# while <condition> -> bool:
#     ...
i = 1
while i <= 10:
    print(i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1


#for -> 知道跑幾次

'''
1.list
l = ['鮭魚','鮪魚','玉子燒']
for index in l:
    print(i)
2.str
for i in 'hello':
    print(i)

3.range(start[init:0], end, interval[init:1]) from start to end-1, increase interval
for i in range(1, 10, 1):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(10):
    print(i)

for i in range(10, 0, -1):
    print(i)
'''
#continue(skip), break(stop)
# for i in range(10):
#     if i % 3 == 0: continue
#     if i == 8: break
#     print(i)

a = [i for i in range(10)]
print(a)