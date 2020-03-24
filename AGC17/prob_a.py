# Problem A - Biscuits

# input
N, P = map(int, input().split())
a_list = list(map(int, input().split()))

# initialization
even_count = 0
odd_count = 0

# count
for a in a_list:
    if a%2==0:
        even_count += 1
    else:
        odd_count = 2 ** (N - 1)
if even_count==len(a_list):
    if P==0:
        print(2 ** N)
    else:
        print(0)
else:
    print(2**(N-1))
