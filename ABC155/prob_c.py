N = int(input())
str_fq_dic = {}
for i in range(N):
    s = input()
    if s in str_fq_dic:
        str_fq_dic[s] = str_fq_dic[s] + 1
    else:
        str_fq_dic[s] = 1

# max value search
max_value = sorted(str_fq_dic.values(), reverse=True)[0]
# max key search
ans_list = []
for s in str_fq_dic:
    if str_fq_dic[s]==max_value:
        ans_list.append(s)

# print output
# alphabet sort
ans_list = sorted(ans_list)
for a in ans_list:
    print(a)
