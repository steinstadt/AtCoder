# Optimal Recommendation
# DP配列がどういう構造になっているかを考えると混乱しそう

N, M = map(int, input().split())
skill_list = [[[0]*101 for i in range(101)] for j in range(101)] # DP用配列の作成

for i in range(N):
    a, b, c, w = map(int,input().split())
    skill_list[a][b][c] = max(skill_list[a][b][c],w)

# skill table update
for a in range(101):
    for b in range(101):
        for c in range(101):
            if not a>=100:
            	skill_list[a+1][b][c] = max(skill_list[a+1][b][c], skill_list[a][b][c])
            if not b>=100:
            	skill_list[a][b+1][c] = max(skill_list[a][b+1][c], skill_list[a][b][c])
            if not c>=100:
            	skill_list[a][b][c+1] = max(skill_list[a][b][c+1], skill_list[a][b][c])

for i in range(M):
    a, b, c = map(int, input().split())
    print(skill_list[a][b][c])
