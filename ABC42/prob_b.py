# Problem B - 文字列大好きいろはちゃん

# input
n, l = map(int, input().split())
s_list = []
for i in range(n):
    s_list.append(input())

# initialization
ans_str = ""
s_list = sorted(s_list)

# integrate
for s in s_list:
    ans_str += s

# output
print(ans_str)
