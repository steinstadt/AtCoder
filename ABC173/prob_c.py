# Problem C - H and V

# input
H, W, K = map(int, input().split())
board = [['']*W for i in range(H)]
for i in range(H):
    s = list(input())
    for j in range(W):
        board[i][j] = s[j]

# pattern
h_pattern = []
w_pattern = []
for i in range(2**H):
    p = [0]*H
    for j in range(H):
        if (i>>j)&1==1:
            p[j] = 1
    h_pattern.append(p)
for i in range(2**W):
    p = [0]*W
    for j in range(W):
        if (i>>j)&1==1:
            p[j] = 1
    w_pattern.append(p)

# initialization
ans = 0


# bit search
for h_p in h_pattern:
    for w_p in w_pattern:
        # 0が塗ってない場合
        tmp = 0
        for i in range(H):
            if h_p[i]==0:
                for j in range(W):
                    if w_p[j]==0 and board[i][j]=='#':
                        tmp += 1
        # check
        if tmp==K:
            ans += 1

# output
print(ans)
