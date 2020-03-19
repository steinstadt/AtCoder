# Problem A - Poisonous Cookies

# input process
A, B, C = map(int, input().split())

# initialization
c_count = 0

# count process
nokori = C - (A + B)
if nokori>0:
    c_count = (A + B) + 1
else:
    c_count = C

# output process
print(c_count + B)
