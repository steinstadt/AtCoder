N, K = map(int, input().split())
digit_str = ''
keta = N
while True:
    keta, amari = keta//K, str(keta%K)
    if keta==0:
        digit_str = digit_str + amari
        break
    digit_str = digit_str + amari

print(len(digit_str))
