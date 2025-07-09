M, D = map(int, input().split()) #['2','3']
S = (M*2+D)%3
l = ['普通','吉','大吉']
print(l[S])