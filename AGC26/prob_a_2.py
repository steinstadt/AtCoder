# Problem A - Colorful Slimes 2

# input process
N = int(input())
a_list = list(map(int, input().split()))

# initialization
magic_num = 0
chohuku_num = 0

# count process
for i in range(0, N):
    if i==0:
        continue

    if a_list[i]==a_list[i-1]:
        chohuku_num += 1
    else:
        magic_num += (chohuku_num + 1) // 2
        chohuku_num = 0
magic_num += (chohuku_num + 1) // 2

print(magic_num)
