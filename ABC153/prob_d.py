# Problem D - Caracal vs Monster

# input
H = int(input())

# initialization
attack_dic = {}

# calc
def calc_count(h, attack):

    if h in attack_dic:
        return attack_dic[h]

    h = h // 2
    if h>0:
        attack += calc_count(h, attack) * 2 + 1
        attack_dic[h] = attack
        return attack
    else:
        return 1
ans = calc_count(H, 0)

# output
print(ans)
