# Problem B - Sum of Three Integers

K, S = map(int, input().split())

count_num = 0
for x in range(K+1):
    tmp_num = S
    tmp_num = tmp_num - x
    for y in range(K+1):
        tmp_num_2 = tmp_num
        z = tmp_num_2 - y
        if z<=K and z>=0:
            count_num = count_num + 1

print(count_num)
