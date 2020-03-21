# Problem B - Common Raccoon vs Monster

# input
h, n = map(int, input().split())
a_list = list(map(int, input().split()))

# initialization
a_sum = sum(a_list)

# output
if h - a_sum<=0:
    print("Yes")
else:
    print("No")
