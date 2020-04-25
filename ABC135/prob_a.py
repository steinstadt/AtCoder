# Problem A - Harmony

# input
A, B = map(int, input().split())

# initialization
K = A + B

# check
if K%2==0:
    K = K // 2
    print(K)
else:
    print("IMPOSSIBLE")
