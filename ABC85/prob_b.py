# Problem B - Kagami Mochi

# input process
N = int(input())
d_list = []
for i in range(N):
    d = int(input())
    d_list.append(d)

d_list = set(d_list)
ans = len(d_list)
print(ans)
