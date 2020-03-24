# Problem E - Dividing Chocolate

# input
H, W, K = map(int, input().split())
board = [['']*W for i in range(H)]
for i in range(H):
    s = list(input())
    for j in range(W):
        board[i][j] = s[j]

# initialization
min_divide = 10**10
s = [0]*(H-1) # 横線の入り方 0:無 1:有
is_ok = True

# search
for i in range(2**(H-1)): # bit全探索
    # sの初期化
    h_count = 0
    w_count = 0
    for j in range(H-1):
        if ((i>>j)&1):
            s[j] = 1
            h_count += 1
        else:
            s[j] = 0

    # 列の全探索
    s_score = [0]*H # 各区域のスコア
    s_cur = [0]*H
    for j in range(W):
        c = 0
        s_cur = [0]*H

        for k in range(H):
            if board[k][j]=='1':
                s_cur[c] += 1

            # Kを超えていないかのチェック
            if s_cur[c]>K:
                is_ok = False
                break

            # 次の遷移先(横線の有無でグループが別れる)
            if k+1<H:
                if s[k]==1:
                    c += 1
        # Kを超えていたらループ中止
        if not is_ok:
            break
        # 前の列のグループと足してみてKを超えていないかチェック
        # 超えていれば縦線分割を施す
        group_smaller = True
        if j>0:
            for c_num in range(c+1):
                if s_score[c_num]+s_cur[c_num]>K:
                    group_smaller = False
        else:
            group_smaller = True

        if group_smaller:
            for c_num in range(c+1):
                s_score[c_num] += s_cur[c_num]
        else:
            w_count += 1
            for c_num in range(c+1):
                s_score[c_num] = s_cur[c_num]

    if not is_ok:
        is_ok = True
        continue

    for c_num in range(h_count+1):
        if s_score[c_num]>K:
            h_count = 10 ** 6

    # 縦線と横線の合計でmin_divideを更新
    min_divide = min(min_divide, w_count + h_count)

# output
print(min_divide)
