n, m = map(int, input().split())

even_cost = 0
odd_cost = 0

if n>=2:
    even_cost = n * (n-1) / 2

if m>=2:
    odd_cost = m * (m-1) / 2

print("%d"%(even_cost + odd_cost))
