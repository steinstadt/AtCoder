a, b = map(int, input().split())

str_a = str(a) * b
str_b = str(b) * a

if str_a<str_b:
    print(str_a)
else:
    print(str_b)
