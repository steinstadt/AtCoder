# Problem Bullet

# input
N = int(input())

# initialization
num_dict = {}
for i in range(N):
    A, B = map(int, input().split())
    tmp_1 = A / B
    tmp_2 = (-1) * B / A
    if tmp_1 in num_dict:
        num_dict[tmp_1] += 1
    else:
        num_dict[tmp_1] = 1

    if tmp_2 in num_dict:
        num_dict[tmp_2] += 1
    else:
        num_dict[tmp_2] = 1
for k in num_dict:
    print(k, num_dict[k])
not_count = 0
total_count = 0
ans = 0

def calc_combi(num):
    tmp_1 = 2**num - num - 1
    tmp_2 = tmp_1 * 2**(N - num)
    return tmp_2

# count
total_count = 2**N - 1
for k in num_dict:
    num = num_dict[k]
    not_count += calc_combi(num)
not_count = not_count // 2
ans = total_count - not_count

# output
print(ans)
