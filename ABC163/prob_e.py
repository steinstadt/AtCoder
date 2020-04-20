# Problem E - Active Infants

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
swaped = {}
swap_count = 0
ans = 0

# swap loop
for i in range(N):
    # スワップ時の最大スコアを計算
    max_score = 0
    swaped_score = 0
    swap_pos = i
    for j in range(N):
        if i==j:
            continue
        # 既にスワップしているposに対して


        tmp = a_nums[i]*abs(i-j) + a_nums[j]*abs(j-i)
        if tmp>max_score:
            max_score = tmp
            swap_pos = j

    # スワップ処理
    swaped[swap_count] = [i, swap_pos]
    swap_count += 1
    ans += max_score
