# Problem B - Touitsu

# input
N = int(input())
A = list(input())
B = list(input())
C = list(input())

# initialization
min_count = 0
cur_char = ''

# string search
for i in range(N):
    tmp = []
    tmp.append(A[i])
    tmp.append(B[i])
    tmp.append(C[i])
    tmp = set(tmp)

    if len(tmp)>=3:
        min_count += 2
    elif len(tmp)==2:
        min_count += 1

# output
print(min_count)
