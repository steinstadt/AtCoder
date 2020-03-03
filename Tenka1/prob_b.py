N = int(input())

min_a = N+1
max_a = 0
max_b = 0

for i in range(N):
    a, b = map(int, input().split())
    # min process
    if a<min_a:
        min_a = a
    # max process
    if a>max_a:
        max_a = a
        max_b = b

ans = (min_a - 1) + (max_a - min_a + 1) + max_b
print(ans)
