N, X = map(int, input().split())
L_list = list(map(int, input().split()))
d_sum = 0
bounce_count = 0

for L in L_list:
    if d_sum+L>X:
        break
    d_sum = d_sum + L
    bounce_count = bounce_count + 1

print(bounce_count+1)
