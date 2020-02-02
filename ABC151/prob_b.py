# Achieve the Goal

# 入力の準備
N, K, M = map(int, input().split())
score_list = list(map(int, input().split()))

goal_sum = N * M # 目標合計点の算出
cur_sum = sum(score_list) # 現在の合計点を算出
goal = goal_sum - cur_sum

if goal<=K and goal>0: # 目標達成可能であれば
    print(goal)
elif goal<=0:
    print(0)
else: # 目標達成不可能であれば
    print(-1)
