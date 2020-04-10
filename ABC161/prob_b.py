# Problem B - Popular Vote

# input
N, M = map(int, input().split())
A_list = list(map(int, input().split()))

# initialization
A_list = sorted(A_list, reverse=True)
is_ok = True
test_limit = sum(A_list) / (4*M)

# check
test_list = A_list[:M]
for t in test_list:
    if t<test_limit:
        is_ok = False
        break

# output
if is_ok:
    print("Yes")
else:
    print("No")
