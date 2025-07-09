# print('kevin', 100)
# print('mary', 70)
# print('alan', 8)

# name = ['kevin', 'mary', 'alan']
# score = [100, 70, 8]
# print(name[0], '的成績是:', score[0])

'''
%
s -> str
d -> int
f -> float
e -> 科學記號
.format
f-string
'''
name, score = ['kevin', 'mary', 'alan'], [100, 70, 8]
print('%5s的成績是:%3d'%(name[0], score[0]))
print('{:5s}的成績是:{:3d}'.format(name[1], score[1])) #. -> 1.的 2.對...做...
print(f'{name[2]:5s}的成績是:{score[2]:3d}')
num = 3.1415926
print(f'{num:5.2f}')
