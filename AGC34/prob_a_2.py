# Problem A - Kenken Race

# input
N, A, B, C, D = map(int, input().split())
S = input()

# initialization
is_ok = True

# search
if C>D:
    # b check
    if "##" in S[B-1:D] or not "..." in S[B-2:D+1]:
        is_ok = False

    # a check
    if "##" in S[A-1:C]:
        is_ok = False
else:
    # b check
    if "##" in S[B-1:D]:
        is_ok = False

    # a check
    if "##" in S[A-1:C]:
        is_ok = False

# output
if is_ok:
    print("Yes")
else:
    print("No")
