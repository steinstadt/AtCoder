# Problem D - DivRem Number

# input
N = int(input())

# initialization
ans = 0

# count
r = 1
while r**2<=N:
    if (N-r)%r==0 and (N-r)/r>r:
        ans += (N-r)//r
    r += 1

# output
print(ans)
