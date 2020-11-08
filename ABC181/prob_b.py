# Problem Trapezoid Sum

# input
N = int(input())

# initialization
ans = 0

# calc
for i in range(N):
    a, b = map(int, input().split())
    tmp = ((b - a + 1) * (a + b)) // 2
    ans += tmp

# output
print(ans)
