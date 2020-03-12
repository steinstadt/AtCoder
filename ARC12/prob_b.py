# Problem B - アキレスと亀

# input process
N, v_a, v_b, L = map(int, input().split())

# calculation process
for n in range(N):
    time_a = L / v_a
    L = v_b * time_a

print("%f"%(L))
