# Problem B - Almost GCD

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
a_max = max(a_list)
ans = -1
ans_num = a_list[0]

# count
for i in range(2, a_max+1):
    tmp = 1
    for a in a_list:
        if a%i==0:
            tmp += 1
    if tmp >= ans:
        ans = tmp
        ans_num = i

# output
print(ans_num)
