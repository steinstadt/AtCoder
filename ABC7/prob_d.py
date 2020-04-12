# Problem D - 禁止された数字

# input
A, B = map(int, input().split())
A -= 1
A = list(str(A))
B = list(str(B))
A = list(map(int, A))
B = list(map(int, B))

# initialization
a_dp = [[[0]*2 for j in range(2)] for k in range(len(A)+1)] # dp[keta][smaller][ok]
a_dp[0][0][0] = 1
b_dp = [[[0]*2 for j in range(2)] for k in range(len(B)+1)] # dp[keta][smaller][ok]
b_dp[0][0][0] = 1

# a digit dp
for keta in range(len(A)): # keta loop
    for s in range(2): # smaller loop
        limit = 0
        if s==0:
            limit = A[keta]
        elif s==1:
            limit = 9
        for x in range(limit + 1):
            if x==4 or x==9:
                a_dp[keta+1][s or x<limit][1] += a_dp[keta][s][0] + a_dp[keta][s][1]
            else:
                a_dp[keta+1][s or x<limit][0] += a_dp[keta][s][0]
                a_dp[keta+1][s or x<limit][1] += a_dp[keta][s][1]
a_ans = a_dp[len(A)][0][1] + a_dp[len(A)][1][1]

# b digit dp
for keta in range(len(B)):
    for s in range(2):
        limit = 0
        if s==0:
            limit = B[keta]
        elif s==1:
            limit = 9
        for x in range(limit + 1):
            if x==4 or x==9:
                b_dp[keta+1][s or x<limit][1] += b_dp[keta][s][0] + b_dp[keta][s][1]
            else:
                b_dp[keta+1][s or x<limit][0] += b_dp[keta][s][0]
                b_dp[keta+1][s or x<limit][1] += b_dp[keta][s][1]
b_ans = b_dp[len(B)][0][1] + b_dp[len(B)][1][1]

# output
ans = b_ans - a_ans
print(ans)
