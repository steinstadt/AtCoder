# Problem B - Bishop

# input process
H, W = map(int, input().split())

if H==1 or W==1:
    print(0)
elif H%2==0: # even count
    print(H//2 * W)
else:
    if not W%2==0:
        even_count = (H//2+1) * (W//2 + 1)
        nokori  = W - W//2 - 1
        odd_count = H//2 * nokori
        print(even_count + odd_count)
    else:
        even_count = (H//2+1) * (W//2 + 1)
        nokori  = W - W//2 - 1
        odd_count = H//2 * nokori
        print(even_count + odd_count -1)
