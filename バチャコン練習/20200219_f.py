N = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

p_num = ""
q_num = ""
for j in range(N):
    p_num = p_num + str(p_list[j])
    q_num = q_num + str(q_list[j])
p_num = int(p_num)
q_num = int(q_num)
p_result_list = []

def perm(p, i, NUM):
    if i<NUM-1: # 脱出条件
        for j in range(i, NUM):
            # スワップ処理
            t = p[i]
            p[i] = p[j]
            p[j] = t

            # n-1個の順列
            perm(p, i+1, NUM)

            # 元に戻すスワップ処理
            t = p[i]
            p[i] = p[j]
            p[j] = t
    else:
        ans_num = ""
        for j in range(0,N):
            ans_num = ans_num + str(p[j])
        ans_num = int(ans_num)
        p_result_list.append(ans_num)

perm(p_list,0,N) # permutation generate
p_result_list = sorted(p_result_list)
p_ord = p_result_list.index(p_num) + 1
q_ord = p_result_list.index(q_num) + 1
print(abs(p_ord-q_ord))
