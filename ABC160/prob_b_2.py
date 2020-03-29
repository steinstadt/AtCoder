# Problem B - Golden Coins

X = int(input())

gohyaku = X // 500
nokori = X % 500
goen = nokori // 5

# output
print(gohyaku * 1000 + goen * 5)
