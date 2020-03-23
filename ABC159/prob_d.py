# Problem D -Banned K

# input
n = int(input())
a_list = list(map(int, input().split()))

# initialization
cur_dic = {}
cur_sum = 0
for a in a_list:
    if a in cur_dic:
        cur_dic[a] += 1
    else:
        cur_dic[a] = 1

for c in cur_dic:
    num = cur_dic[c]
    cur_sum += num * (num-1) / 2

for i in range(len(a_list)):
    a = a_list[i]
    d = cur_dic[a]
    # 減らす
    if d > 1:
        cur_sum -= d * (d-1) / 2
    cur_dic[a] -= 1

    # output
    tmp = cur_sum
    if cur_dic[a] > 1:
        tmp = cur_sum + cur_dic[a] * (cur_dic[a] - 1) / 2 # update
    print("%d"%(tmp))

    # 増やす
    if d > 1:
        cur_sum += d * (d-1) / 2
    cur_dic[a] += 1
