# Problem B

# input
N, A, B = map(int, input().split())

# initialization
num_sa = N // (A+B)
num_amari = N % (A+B)

# process
ans_1 = num_sa * A
if num_amari>A:
    num_amari = A
ans_2 = ans_1 + num_amari

# output
print(ans_2)
