
# first input
a_1, a_2, a_3 = map(int, input().split())
a_4, a_5, a_6 = map(int, input().split())
a_7, a_8, a_9 = map(int, input().split())

a_list = []

a_list.append([a_1, a_2, a_3])
a_list.append([a_4, a_5, a_6])
a_list.append([a_7, a_8, a_9])
a_list.append([a_1, a_4, a_7])
a_list.append([a_2, a_5, a_8])
a_list.append([a_3, a_6, a_9])
a_list.append([a_1, a_5, a_9])
a_list.append([a_3, a_5, a_7])

N = int(input())
for i in range(N):
    b = int(input())
    for a in a_list:
        if b in a:
            a.pop(a.index(b))

ans = False
for a in a_list:
    if len(a)==0:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
