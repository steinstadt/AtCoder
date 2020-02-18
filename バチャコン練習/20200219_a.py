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

N, P = map(int, input().split())
p_fact = factorization(P)
p_list = []
ans = 1
for p in p_fact:
    p[1] = p[1] // N
    p_list.append(p)

for p in p_list:
    ans = ans * pow(p[0], p[1])

print(ans)
