# Problem A - Biscuits

# input
N, P = map(int, input().split())
a_nums = list(map(int, input().split()))

# initialization
even_count = 0
odd_count = 0
for a in a_nums:
    if a%2==0:
        even_count += 1
    else:
        odd_count += 1

# check
if even_count==N:
    if P==0:
        print(2**N)
    else:
        print(0)
else:
    print(2**(N-1))
