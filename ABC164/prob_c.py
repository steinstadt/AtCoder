# Problem C - gacha

# input
n = int(input())
s_list = []
for i in range(n):
    s_list.append(input())

# initialization
s_list = list(set(s_list))
ans = len(s_list)

# output
print(ans)
