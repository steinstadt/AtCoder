# Problem B - String Rotation

S = input()
T = input()
is_same = False

for i in range(len(S)):
    S = S[-1] + S[:-1]
    if S==T:
        is_same = True
        break

if is_same:
    print("Yes")
else:
    print("No")
