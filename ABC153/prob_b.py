# Problem B - Common Raccoon vs Monster

# input
H, N = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
a_sum = sum(a_nums)

# output
if a_sum>=H:
    print("Yes")
else:
    print("No")
