# Problem B - 細長いお菓子

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
max_len = 0

# shakutori count
right = 0
cur_set = set([])
for left in range(N):
    while right<N and not a_list[right] in cur_set:
        cur_set.add(a_list[right])
        right += 1

    max_len = max(max_len, right - left)

    # left update
    if left==right:
        right += 1
    else:
        cur_set.remove(a_list[left])

# output
print(max_len)
