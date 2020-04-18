# Problem E - Dividing Chocolate

# input
H, W, K = map(int, input().split())
board = [[0]*W for i in range(H)]
for i in range(H):
    s = list(input())
    for j in range(W):
        board[i][j] = int(s[j])

# initialization
min_divide = 10**15

# pattern search
for i in range(2**(H-1)):
    # bit search
    h_pattern = [0]*(H-1)
    group_count = 1
    h_count = 0
    w_count = 0
    for j in range(H-1):
        if((i>>j)&1):
            h_pattern[j] = 1
            group_count += 1
            h_count += 1

    is_ok = True
    group_sum = [0]*group_count
    for w in range(W):
        cur_count = [0]*group_count
        cur_count_num = 0
        # 列そのものが条件を満たしているかチェック
        for h in range(H):
            if board[h][w]==1:
                cur_count[cur_count_num] += 1

            if cur_count[cur_count_num]>K:
                is_ok = False
                break

            if h<H-1 and h_pattern[h]==1:
                cur_count_num += 1

        if not is_ok:
            break

        # 現在の列をグループカウントに入れる
        is_smaller = True
        if w==0:
            is_smaller = True
        else:
            for c in range(group_count):
                if group_sum[c]+cur_count[c]>K:
                    is_smaller = False
        if is_smaller:
            for c in range(group_count):
                group_sum[c] += cur_count[c]
        else:
            # wで区切る
            for c in range(group_count):
                group_sum[c] = cur_count[c]
            w_count += 1

    if not is_ok:
        is_ok = True
        continue

    # update
    min_divide = min(min_divide, h_count + w_count)

# output
print(min_divide)
