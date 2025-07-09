#seprate -> sep 分隔符號(init:空格)
#end 結尾符號(init:'\n'->換行)
print(1)
print('hi',end=' ')
print(7*8)
print('hi',123,'hello',9+8, sep='@')

#input: alan, output: hi, alan
print('hi,',input('請輸入姓名')) # -> str

l = input().split() #'5 10' ->l = ['5','10']
#. 1.的 2.對...做...