# Problem A - 数え上げ

# input process
N = int(input())

# initialization
S = ["1"]

# count process
for i in range(N):
    S.append("0")
S[N] = "7"

# output process
print("".join(S))
