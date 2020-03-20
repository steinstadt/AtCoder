# Problem B - Resistors in Parallel

# input
n = int(input())
a_list = list(map(int, input().split()))

# initialization
tmp_sum = 0

# sum
for a in a_list:
    tmp_sum += 1 / a

# output
print(1 / tmp_sum)
