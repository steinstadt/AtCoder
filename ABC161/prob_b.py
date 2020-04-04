# Problem B
N, M = map(int, input().split())
A_list = list(map(int, input().split()))

# initialization
a_sum = sum(A_list)
a_limit = a_sum / (4*M)
a_count = 0
is_ok = False

# search
for a in A_list:
    if a>=a_limit:
        a_count += 1

# output
if a_count>=M:
    print("Yes")
else:
    print("No")
