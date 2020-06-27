# Problem B - RGB Boxes

# input
r, g, b, n = map(int, input().split())

# initialization
count = 0

# count
for i in range(n+1):
    for j in range(n+1):
        if n-r*i-g*j<0:
            continue
        k = 0
        if (n-r*i-g*j)%b==0:
            k = (n-r*i-g*j)//b
        if (r*i + g*j + b*k)==n:
            count += 1

# output
print(count)
