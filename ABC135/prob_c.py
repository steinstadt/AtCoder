N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
monster_count = 0

for i in range(N):
    a_1, a_2 = A_list[i], A_list[i+1]
    b = B_list[i]
    if b>=a_1:
        monster_count = monster_count + a_1
        b = b - a_1
    elif b<a_1:
        monster_count = monster_count + b
        continue

    if b>=a_2:
        monster_count = monster_count + a_2
        A_list[i+1] = 0
    elif b<a_2:
        monster_count = monster_count + b
        a_2 = a_2 - b
        A_list[i+1] = a_2

print(monster_count)
