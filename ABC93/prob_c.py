# Problem C - Same Integers

# input
A, B, C = map(int, input().split())

# initialization
num_list = sorted([A, B, C])
sa = num_list[2] - num_list[1]
count = sa

# count 1
for i in range(3):
    if num_list[i]<num_list[2]:
        num_list[i] += sa

# count 2
num_list = sorted(num_list)
if num_list[0]<num_list[1] and num_list[0]<num_list[2]:
    if (num_list[1]-num_list[0])%2==0:
        count += (num_list[1]-num_list[0])// 2
    else:
        count += (num_list[1]-num_list[0])// 2 + 2
elif num_list[2]>num_list[0] and num_list[2]>num_list[1]:
    count += 1

# output
print(count)
