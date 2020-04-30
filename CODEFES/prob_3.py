# Problem C - 2月29日

# input
A, B = map(int, input().split())

# check
ans = 0

# func
def calc(n):
    num_4 = n // 4
    num_100 = n // 100
    num_400 = n // 400
    return num_4 - num_100 + num_400

# count
ans = calc(B) - calc(A - 1)

# output
print(ans)
