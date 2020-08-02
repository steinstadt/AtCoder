# Problem B - Magic 2

# input
A, B, C = map(int, input().split())
K = int(input())

# B check
while B<=A:
    B = B * 2
    K -= 1

# C check
while C<=B:
    C = C * 2
    K -= 1

# output
if K>=0:
    print("Yes")
else:
    print("No")
