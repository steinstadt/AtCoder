# Problem A - 2倍チェック

# input
S = input()
S_len = len(S)

# initialization
is_ok = True
num_list = [str(i) for i in range(10)]

# count
for i in range(S_len):
    if not S[i] in num_list:
        is_ok = False

# output
if is_ok:
    print(int(S)*2)
else:
    print("error")
