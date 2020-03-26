# Problem A - Kenken Race

# input
N, A, B, C, D = map(int, input().split())
S = list(input())

# check
if C<D:
    # B check
    is_ok = True
    for i in range(B, D-1):
        if S[i]=='#' and S[i+1]=='#':
            is_ok = False
            break
    # A check
    for i in range(A, C-1):
        if S[i]=='#' and S[i+1]=='#':
            is_ok = False
            break
    # output
    if is_ok:
        print("Yes")
    else:
        print("No")
else:
    is_ok = False
    # B check
    for i in range(B, D):
        if S[i]=='#' and S[i+1]=='#':
            is_ok = False
            break
    for i in range(B-1, D):
        if S[i-1]=='.' and S[i]=='.' and S[i+1]=='.':
            is_ok = True
    # A check
    for i in range(A, C-1):
        if S[i]=='#' and S[i+1]=='#':
            is_ok = False
            break
    # output
    if is_ok:
        print("Yes")
    else:
        print("No")
