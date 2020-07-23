# A - B problem
# input
nums = list(input().split())

# initialization
max_ans = -1 * float("INF")
nums = list(map(list, nums))

def calc_score(t1, t2, n):
    if n==0:
        a = int("".join(t1))
        b = int("".join(t2))
        return a - b
    else:
        a = int("".join(t1))
        b = int("".join(t2))
        return b - a

# check
for k in range(3):
    for n in range(2):
        tmp1 = nums[n]
        tmp2 = nums[(n+1)%2]
        if k==0: # 1桁目であれば
            for i in range(2):
                if i==0:
                    b = tmp1[k]
                    tmp1[k] = '1'
                    max_ans = max(max_ans, calc_score(tmp1, tmp2, n))
                    tmp1[k] = b
                else:
                    b = tmp1[k]
                    tmp1[k] = '9'
                    max_ans = max(max_ans, calc_score(tmp1, tmp2, n))
                    tmp1[k] = b
        else:
            for i in range(2):
                if i==0:
                    b = tmp1[k]
                    tmp1[k] = '0'
                    max_ans = max(max_ans, calc_score(tmp1, tmp2, n))
                    tmp1[k] = b
                else:
                    b = tmp1[k]
                    tmp1[k] = '9'
                    max_ans = max(max_ans, calc_score(tmp1, tmp2, n))
                    tmp1[k] = b

# output
print(max_ans)
