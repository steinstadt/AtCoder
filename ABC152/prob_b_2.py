# Problem B - Comparing Strings

# input process
a, b = input().split()

str_a = a * int(b)
str_b = b * int(a)

# output process
if str_a>=str_b:
    print(str_b)
else:
    print(str_a)
