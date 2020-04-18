# Problem D - Boring Sequence

from collections import Counter

# input
N, K = map(int, input().split())
a_list = list(map(int, input().split()))
a_len = len(a_list)

# initialization
ct = Counter(a_list)
left = 0
right = ct.most_common()[0][1]

# binary search
while not abs(right-left)<=1:
    mid = (right + left) // 2

    num_count = 1
    update_count = 0
    i = 1
    while i<N:
        if a_list[i-1]==a_list[i]:
            num_count += 1
            if num_count>mid:
                update_count += 1
                num_count = 1
                i += 1
        else: # 等しくなかったときの処理
            num_count = 1

        i += 1


    if update_count<=K:
        right = mid
    else:
        left = mid

# output
print(right)
