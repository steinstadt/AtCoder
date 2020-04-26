# Problem B - Picture Frame

# input
H, W = map(int, input().split())
a_list = [['']*W for i in range(H)]
for i in range(H):
    a_nums = list(input())
    for j in range(W):
        a_list[i][j] = a_nums[j]

# output
ans = "#"*(W+2)
ans += "\n"
for i in range(H):
    ans += "#"
    for j in range(W):
        ans += a_list[i][j]
    ans += "#\n"
ans += "#"*(W+2)
print(ans)
