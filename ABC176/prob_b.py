# Problem B - Multiple of 9

# input
n = list(input())

# initialization
check_num = 0

# check
for c in n:
    check_num += int(c)

# output
if check_num%9==0:
    print("Yes")
else:
    print("No")
