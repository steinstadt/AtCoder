# Problem B - Digit Sums

# input
N = input()
N_str = list(N)
N_num = int(N)

# initialization
digit_sum = 0

# count
for n in N_str:
    tmp = int(n)
    digit_sum += tmp

# check
if N_num%digit_sum==0:
    print("Yes")
else:
    print("No")
