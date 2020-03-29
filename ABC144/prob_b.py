# Problem B - 81

# input
N = int(input())

# initialization
num_list = []
for i in range(1, 10):
    for j in range(1, 10):
        num_list.append(i * j)
num_list = list(set(num_list))

# output
if N in num_list:
    print("Yes")
else:
    print("No")
