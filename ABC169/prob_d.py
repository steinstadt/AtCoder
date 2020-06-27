# Problem D - Div Game

# input
N = int(input())

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

# check
if N==1:
    print(0)
else:
    count = 0
    fact_list = factorization(N)
    for f in fact_list:
        tmp = f[1]
        i = 1
        while tmp-i>=0:
            count += 1
            tmp -= i
            i += 1
    print(count)
