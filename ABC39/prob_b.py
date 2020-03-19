# Problem B - エージェント高橋君

# input process
X = int(input())

# initialization
ans = 0

# count process
for i in range(1000):
    tmp = i ** 4
    if tmp==X:
        ans = i
        break

# output process
print(ans)
