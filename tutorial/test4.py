a, b = map(int, input().split())

a_str = str(a)*b
b_str = str(b)*a

if a_str <= b_str:
    print(a_str)
else:
    print(b_str)
