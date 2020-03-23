# Problem C - 飛行機乗り

# input
N, M = map(int, input().split())
X, Y = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# initialization
step_count = 0
air_flag = True # True:A, False:B
air_time = 0
a_i = 0 # time
b_i = 0 # time

# count
while True:
    if air_flag: # A pattern
        if a_i<N:
            a = a_list[a_i]
            if a>=air_time:
                # 乗車
                air_time = a + X
                a_i += 1
                air_flag = False
            else:
                a_i += 1
        else:
            break
    else: # B pattern
        if b_i<M:
            b = b_list[b_i]
            if b>=air_time:
                # 乗車
                air_time = b + Y
                b_i += 1
                air_flag = True
                step_count += 1
            else:
                b_i += 1
        else:
            break

# output
print(step_count)
