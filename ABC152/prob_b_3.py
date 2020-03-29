# Problem B - Comparing Strings

# input
a, b = map(int, input().split())

# initialization
a_str = str(a) * b
b_str = str(b) * a

# output
if a_str<=b_str:
    print(a_str)
else:
    print(b_str)
