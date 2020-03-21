# Problem A - Candy Distribution Again

# input
n, x = map(int, input().split())
a_list = list(map(int, input().split()))

# initialization
a_list = sorted(a_list)
person_num = 0

# count process
for i in range(len(a_list)):
    a = a_list[i]
    x = x - a
    if x >= 0:
        person_num += 1

# output
if x>0:
    print(person_num - 1)
else:
    print(person_num)
