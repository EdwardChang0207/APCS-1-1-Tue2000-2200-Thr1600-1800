x, n = map(int, input().split())
f = list(map(int,input().split()))
right = 0
#x如果放入f中，他是第幾大 (y)？ -> y >= len(f)/2
for i in f:
    if i > x: right += 1

#如果往右->最右邊的食物
if right > (n-right):
    print(right, max(f))
#如果往左->最左邊的食物
if right < (n-right):
    print(n-right, min(f))
