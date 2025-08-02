n = int(input())
# score = [int(i) for i in input().split()]
score = list(map(int, input().split()))
score.sort()
# for i in score:
#     print(i, end= ' ')
print(*score)
#best
if score[0] >= 60:
    print('best case')
    print(score[0])
#worst
elif score[-1] < 60:
    print(score[-1])
    print('worst case')
#normal
else:
    for i in range(len(score)):
        if score[i] >= 60:
            print(score[i-1])
            print(score[i])
            break