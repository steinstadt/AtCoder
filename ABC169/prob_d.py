# Problem D - Div Game

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# input
N = int(input())

# initialization
fact_arr = factorization(N)
count = 0

# count
for f in fact_arr:
    c = f[1]
    tmp_count = 0
    i = 1
    while c-i>=0:
        c -= i
        tmp_count += 1
        i += 1
    count += tmp_count

# output
if N==1:
    count = 0
print(count)
