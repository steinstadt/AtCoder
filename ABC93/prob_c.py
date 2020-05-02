# Problem C - Same Integers

# input
A, B, C = map(int, input().split())

# initialization
num_count = 0
not_finished = True
ans_list = [A, B, C]

# count
while not_finished:
    if ans_list[0]==ans_list[1] and ans_list[1]==ans_list[2]:
        not_finished=False
        break
    ans_list = sorted(ans_list)
    if len(set(ans_list))==3:
        ans_list[0] += 1
        ans_list[1] += 1
        num_count += 1
    elif ans_list[1]==ans_list[2]:
        ans_list[0] += 2
        num_count += 1
    elif ans_list[0]==ans_list[1]:
        ans_list[0] += 1
        ans_list[1] += 1
        num_count += 1

# output
print(num_count)
