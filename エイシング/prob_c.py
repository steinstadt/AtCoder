# Problem XYZ Triplets

# input
N = int(input())

# initialization
ans_list = [0]*(10**6)

# calc
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x
            ans_list[tmp] += 1

# output
for i in range(1, N+1):
    print(ans_list[i])
