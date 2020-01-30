# Handstand 2

N = int(input())
count = 0

count_list = [[0]*10 for i in range(10)]

# 1~Nまでの先頭iと末尾jの頻度を全て算出する
for a in range(1,N+1):
    a_str = str(a)
    a_i, a_j = int(a_str[0]), int(a_str[-1]) # 各数の先頭桁を求める
    count_list[a_i][a_j] = count_list[a_i][a_j] + 1

# count_listから全ての組み合わせ数を計算
for i in range(1,10):
    for j in range(1,10):
        count = count + count_list[i][j]*count_list[j][i]

print(count)
