N = int(input())
X_list = list(map(int, input().split()))

min_n = min(X_list)
max_n = max(X_list)
min_cost = 10**16

for n in range(min_n,max_n+1):
    cost = 0
    for x in X_list:
        cost = cost + (x - n)**2
    min_cost = min(min_cost, cost)

print(min_cost)
