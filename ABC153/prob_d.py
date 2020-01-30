H = int(input())

memo_count = {}
def searchCount(h):
    if h==1: # 脱出条件
        return 1
    elif h in memo_count:
        return memo_count[h]
    else:
        h_half = int(h / 2)
        memo_count[h] = 1 + 2*searchCount(h_half)
        return memo_count[h]

print(searchCount(H))
