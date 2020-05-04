# Problem E - This Message Will Self-Destruct

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
num_dic = {}
ans = 0

# count
for i in range(1, N+1):
    a = a_nums[i-1] + i
    if not a in num_dic:
        num_dic[a] = 1
    else:
        num_dic[a] += 1

# count 2
for j in range(1, N+1):
    b = j - a_nums[j-1]
    if b in num_dic:
        ans += num_dic[b]

# output
print(ans)
