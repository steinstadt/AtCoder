# Problem D - Lunlun Number

# input
K = int(input())

# initialization
ans = [-1]*18

def num_add(num_list, i):
    if not num_list[i+1]==-1 and abs(num_list[i]+1-num_list[i+1])<=1:
        num_list[i] += 1
    elif num_list[i+1]==-1 and num_list[i]<9:
        num_list[i] += 1
        return num_list
    elif num_list[i]==9:
        if num_list[i+1]==-1:
            num_list[i+1] = 1
            num_list[i] = 0
        else:
            num_add(num_list, i+1)
            num_list[i] = 0
        return num_list
    else:
        num_add(num_list, i+1)
        tmp = num_list[i+1] - 1
        if tmp<=0:
            tmp = 0
        num_list[i] = tmp
    return num_list

for i in range(K+1):
    # 1桁台の場合
    if i<=9:
        ans[0] += 1
        continue

    if i==10:
        ans[1] = 1
        ans[0] = 0
        continue

    # 2桁以降の場合(桁付き足し算)
    ans = num_add(ans, 0)

# output
for i in range(len(ans)):
    if ans[i]==-1:
        ans[i] = 0
ans = float("".join(map(str,ans[::-1])))
print(ans)
