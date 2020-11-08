# Problem D - Hachi
from itertools import permutations

# input
S = list(input())

# initialization
ans = False

def conv_nums(nums):
    num_list = [0] * 10
    conv_result = []
    for n in nums:
        num_list[n] += 1
    for i in range(1, 10):
        if num_list[i]==0:
            continue
        if num_list[i]>3:
            num_list[i] = 3
        for j in range(num_list[i]):
            conv_result.append(str(i))
    return conv_result

def check_eight(num):
    if not num%2==0:
        return False
    tmp_1 = num // 2
    tmp_1 = str(tmp_1)
    tmp_1 = int(tmp_1[-2] + tmp_1[-1])
    if not tmp_1%4==0:
        return False
    return True


# check
if len(S)==1:
    tmp = int(S[0])
    if tmp%8==0:
        ans = True
elif len(S)==2:
    tmp = int(S[0] + S[1])
    if tmp%8==0:
        ans = True
    tmp = int(S[1] + S[0])
    if tmp%8==0:
        ans = True
else:
    T = list(map(int, S))
    T = conv_nums(T) # 数字の集合をまとめる
    T_len = len(T)
    for i in range(T_len-2):
        for j in range(i+1, T_len-1):
            for k in range(j+1, T_len):
                tmp_list = [T[i], T[j], T[k]]
                for tmp_p in permutations(tmp_list):
                    check_result = check_eight(int("".join(tmp_p)))
                    if check_result:
                        ans = True

# output
if ans:
    print("Yes")
else:
    print("No")
