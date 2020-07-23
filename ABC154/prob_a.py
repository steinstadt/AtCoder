# Problem A - Remaining Balls

# input
S, T = input().split()
A, B = map(int, input().split())
U = input()

# check
if U==S:
    A -= 1
else:
    B -= 1

# output
print(A, B)
