# Problem A - ABC Swap

# input
X, Y, Z = map(int, input().split())

# swap
tmp = X
X = Y
Y = tmp
tmp = X
X = Z
Z = tmp

# output
print("%d %d %d"%(X, Y, Z))
