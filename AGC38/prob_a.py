# Problem A - 01 Matrix

# input
H, W, A, B = map(int, input().split())

for i in range(1, H+1):
    for j in range(1, W+1):
        if i<=B and j<=A:
            print('0', end="")
        elif i<=B and j>A:
            print('1', end="")
        elif i>B and j<=A:
            print('1', end="")
        elif i>B and j>A:
            print('0', end="")
    print()
