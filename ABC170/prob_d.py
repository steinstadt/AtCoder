# Problem D - Not Divisible
# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
max_a = max(a_nums)
fact_list = [0] * (max_a + 1)
ans = 0

# count
for a in a_nums:
    tmp = max_a // a
    for i in range(tmp):
        fact_list[a*(i+1)] += 1

# count 2
for a in a_nums:
    if fact_list[a]==1:
        ans += 1

# output
print(ans)
