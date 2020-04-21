# Problem C - Not so Diverse

from collections import Counter

# input
N, K = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
a_sets = set(a_nums)
a_len = len(a_sets)

# output
if a_len-K<=0:
    print(0)
else:
    # 色を変える必要がある場合
    a_counter = Counter(a_nums)
    a_counter = a_counter.most_common()[::-1]

    # count
    ans = 0
    for i in range(a_len - K):
        ans += a_counter[i][1]
    print(ans)
