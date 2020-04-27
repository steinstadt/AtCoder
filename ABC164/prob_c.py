# Problem C - gacha

# input
N = int(input())
s_list = []
for i in range(N):
    s = input()
    s_list.append(s)

# initialization
ans = len(set(s_list))

# output
print(ans)
