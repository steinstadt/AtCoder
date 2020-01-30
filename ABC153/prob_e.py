# ダイナミック・プログラミング(DP)

H, N = map(int, input().split())
magic_list = []

for i in range(N):
    A, B = map(int, input().split())
    magic_list.append([A, B])


dp_memo = {} # メモ化再帰
def dp_magic_2(HP):
    mp_list = []
    if HP<=0:
        return 0
    elif HP in dp_memo:
        return dp_memo[HP]
    else:
        for m in magic_list:
            mp_list.append(dp_magic_2(HP-m[0]) + m[1])
        result_mp = sorted(mp_list)[0]
        dp_memo[HP] = result_mp
        return result_mp

print(dp_magic_2(H))
