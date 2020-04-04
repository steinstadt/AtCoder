# Problem A

A, B, C = map(int, input().split())

tmp = B
B = A
A = tmp
tmp = A
A = C
C = tmp

# output
print("%d %d %d"%(A, B, C))
