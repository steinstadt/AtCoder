# 最小値探索

N = int(input())
p_list = list(map(int, input().split()))

count = 0 # p_j > p_i である回数
p_length = len(p_list)
p_min = p_list[0] # 現時点での最小値

for i in range(p_length):
    if p_list[i]<=p_min:
        p_min = p_list[i]
        count = count + 1 # カウントを１つ増やす
    else:
        continue

print(count)
