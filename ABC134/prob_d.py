# Problem D - Preparing Boxes

# input and initialization
N = int(input())
a_list = list(map(int, input().split()))
current_num = [0]*N

M = 0
b_list = []
is_equivalent = True

for i in reversed(range(1,N+1)):
    num = 1
    for j in range(i,N+1,i):
        if current_num[j-1]==1:
            num = num + 1
    if num%2==a_list[i-1]:
        current_num[i-1] = 1

for i in range(N):
    if current_num[i]>=1:
        M = M + 1
        b_list.append(i+1)

# output process
print(M)
for b in b_list:
    print(b, end=" ")
