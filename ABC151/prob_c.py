# Welcome to AtCoder

# 入力の準備
N, M = map(int, input().split())
result_list = []
for i in range(M):
    result_list.append(input().split())

ans_num = 0 # 正答数
penalty_num = 0 # ペナルティ数

correct_memo = {} # 正答されたものを保管するメモ
penalty_memo = [0 for i in range(N+1)] # ペナルティ数のメモ

for r in result_list:
    key = int(r[0])
    if key in correct_memo: # すでにACが出ていればスキップ
        continue

    if r[1]=='WA': # ペナルティ数のメモ
        penalty_memo[key] = penalty_memo[key] + 1
    elif r[1]=='AC':
        correct_memo[key] = 1 # メモをしておく
        ans_num = ans_num + 1
        penalty_num = penalty_num + penalty_memo[key]

print(ans_num, penalty_num)
