# Problem B - Shiritori

# input
N = int(input())

# initialization
last = input()
word_list = []
word_list.append(last)
is_ok = True

# search
for i in range(N-1):
    tmp = input()
    if tmp in word_list or not last[-1]==tmp[0]:
        is_ok = False
        break
    else:
        last = tmp
        word_list.append(tmp)

# output
if is_ok:
    print("Yes")
else:
    print("No")
