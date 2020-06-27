# Problem E - Red Scarf

# input
N = int(input())
a_nums = list(map(int, input().split()))

# initialization
xor_sum = 0
# xor sum
for a in a_nums:
    xor_sum = xor_sum ^ a
ans = []

# xor check
for a in a_nums:
    tmp = xor_sum ^ a
    ans.append(tmp)

# output
print(" ".join(list(map(str, ans))))
