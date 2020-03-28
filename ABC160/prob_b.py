X = int(input())

gohyaku = X//500
nokori = X % 500
goen = nokori//5

print(gohyaku*1000 + goen*5)
