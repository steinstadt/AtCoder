# Problem C - 高橋君と魔法の箱

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
b_list = []

# count
for i in range(N):
    b = a_list[i]

    while b%2==0:
        b = b // 2

    b_list.append(b)

# output
b_list = set(b_list)
print(len(b_list))
