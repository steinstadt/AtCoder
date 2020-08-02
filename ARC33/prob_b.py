# Problem B - メタ構文変数

# input
na, nb = map(int, input().split())
a_nums = set(list(map(int, input().split())))
b_nums = set(list(map(int, input().split())))

# intersection calc
s1 = a_nums & b_nums

# union calc
s2 = a_nums | b_nums

# output
ans = len(s1) / len(s2)
print(ans)
