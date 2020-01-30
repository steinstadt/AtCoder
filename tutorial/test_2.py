s = input()

one_count = 0
if not len(s)==3:
    print("Error")
else:
    for i in range(3):
        if s[i]=='1':
            one_count = one_count + 1

print(one_count)
