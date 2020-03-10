# Problem A - +-x

A, B = map(int, input().split())
num_list = []

num_list.append(A-B)
num_list.append(A+B)
num_list.append(A*B)

ans_max = max(num_list)
print(ans_max)
