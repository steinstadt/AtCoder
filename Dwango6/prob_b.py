# Fusing Slimes
import random

e = 10**9 + 7 # 大きい数の対策

N = int(input())
x_list = list(map(int, input().split()))

# 操作をN-1回行う(計算量O(N))
kitai = 0 # 期待値
dist = 0 # 移動距離
kaijo = 1 # 階乗計算
for i in range(N-1):
    print(x_list)
    length = len(x_list) # 現時点でのリスト長を取得
    p = random.randint(0,length-2) # 1~N-1を等確率で選択
    d = x_list[p+1] - x_list[p]
    dist = dist + d # 移動距離の格納
    kitai = kitai + d / (length-1)
    kaijo = kaijo * (i+1)
    x_list.pop(p) # リストから要素を取り除く

ans = (kitai * kaijo) % e
print(ans)
