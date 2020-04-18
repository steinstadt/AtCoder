# Problem B - 花束

# input
R, B = map(int, input().split())
x, y = map(int, input().split())

# initialization
left = 0
right = (R + B)//2 + 1

# binary search
while not abs(right-left)<=1:
    mid = (right + left)//2

    count_r = R - mid
    count_b = B - mid
    if count_r<0 or count_b<0: # 確保もできないということ
        right = mid
        continue

    test_r = count_r // (x - 1)
    test_b = count_b // (y - 1)
    kosu = test_r + test_b
    # check
    if kosu>=mid:
        left = mid
    else:
        right = mid

# output
print(left)
