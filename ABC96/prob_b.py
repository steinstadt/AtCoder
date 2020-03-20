# Problem B - Maximum Sum

# input
a, b, c = map(int, input().split())
k = int(input())

# initialization
max_cost = 0

# max index search
if a>=b and a>=c:
    for i in range(k):
        a = a * 2
elif b>=a and b>=c:
    for i in range(k):
        b = b * 2
elif c>=a and c>=b:
    for i in range(k):
        c = c * 2

ans = a + b + c
print(ans)
