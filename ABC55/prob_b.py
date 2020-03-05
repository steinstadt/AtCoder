# Problem B - Training Camp

# input process
N = int(input())

# initialization
frac_num = 1
INF = 10**9 + 7

for i in range(1, N+1):
    frac_num = frac_num * i

print(frac_num%INF)
