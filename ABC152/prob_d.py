# Handstand 2
# TLEにより失敗
# c_ij = {1<=k<=N : 先頭の桁がiで、末尾の桁の数がjであるもの}

N = int(input())
count = 0

# 先頭の桁をi, 末尾の桁をjとする数の数を求める
c_memo = {}
def c(i, j):
    count_num = 0
    key = str(i) + '_' + str(j)
    if key in c_memo:
        return c_memo[key]
    for a in range(1,N+1):
        a_str = str(a)
        a_i, a_j = int(a_str[0]), int(a_str[-1]) # 各数の先頭桁を求める
        if i==a_i and j==a_j:
            count_num = count_num + 1
    c_memo[key] = count_num
    return count_num


for i in range(10):
    for j in range(10):
        count += c(i,j)*c(j,i)

print(count)
