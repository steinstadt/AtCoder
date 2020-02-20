N, M, K = map(int, input().split())
is_k = False
for k in range(N+1):
    for l in range(M+1):
        c = k*(M-l)+l*(N-k)
        if c==K:
            is_k = True

if is_k:
    print("Yes")
else:
    print("No")
