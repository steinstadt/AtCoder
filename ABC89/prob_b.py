N = int(input())
S_list = list(input().split())

ans = False
for s in S_list:
    if s == "Y":
        ans = True
        break

if ans:
    print("Four")
else:
    print("Three")
