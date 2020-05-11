# Problem D - Teleporter

# input
N, K = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
visit_list = [0]*N
visit_list[0] = 1
pos = a_nums[0]
visit_count = 1

while visit_list[pos-1]==0 and visit_count<K:
    visit_count += 1
    visit_list[pos-1] = visit_count
    pos = a_nums[pos-1]
visit_count += 1

# calc 1
if visit_count<K:
    tmp_1 = 0
    if pos==1:
        tmp_1 = visit_count - visit_list[pos-1] # 周期
    else:
        tmp_1 = visit_count - visit_list[pos-1]
    tmp_2 = (K-visit_count) % tmp_1 # 何周するのか
    # tmp_2回分ループ処理を行う
    for i in range(tmp_2+1):
        pos = a_nums[pos-1]

# output
print(pos)
