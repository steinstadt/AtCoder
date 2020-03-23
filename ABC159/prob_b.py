s = input()

s_len = len(s)
s_1 = s[:(s_len-1)//2]
s_2 = s[(s_len+3)//2-1:]
test_1 = s
test_2 = s[::-1]

is_ok = True

if not test_1==test_2:
    is_ok = False

if not s_1==s_1[::-1]:
    is_ok = False

if not s_2==s_2[::-1]:
    is_ok = False

if is_ok:
    print("Yes")
else:
    print("No")
