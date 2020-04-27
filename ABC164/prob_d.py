# Problem D - Multiple of 2019

# input
S = list(input())
N = len(S)

# initialization
ans = 0

# count
nums_2019 = [0]*2019
nums_2019[0] = 1
s = 0
for i in range(N-1, -1, -1):
    s += int(S[i]) * pow(10, N - i - 1, 2019)
    nums_2019[s%2019] += 1

for i in range(2019):
    if nums_2019[i]>=2:
        ans += nums_2019[i] * (nums_2019[i]-1) // 2

# output
print(ans)
