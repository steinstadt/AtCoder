# Problem A - Odds of Oddness

# input process
N = int(input())

# initialization
count = 0

# count process
for i in range(1, N+1):
    if not i%2==0:
        count += 1

print(count/N)
