# Problem C - 数を3つ選ぶマン

# input process
num_list = list(map(int, input().split()))

# initialization
ans_list = []

for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            tmp = num_list[i] + num_list[j] + num_list[k]
            ans_list.append(tmp)
ans_list = list(set(ans_list))
ans_list = sorted(ans_list, reverse=True)

# output process
print(ans_list[2])
