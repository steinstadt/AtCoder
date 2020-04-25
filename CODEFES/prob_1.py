# Problem B - Exactly N points(Code Festival)

# input
N = int(input())

# initialization
ans_list = []
check_sum = 0

# count
for i in range(1, N+1):
    check_sum += i
    ans_list.append(i)
    if check_sum>=N:
        tmp_sum = sum(ans_list)
        remove_num = check_sum - N
        if remove_num in ans_list:
            ans_list.remove(remove_num)
        break

# output
for a in ans_list:
    print(a)
