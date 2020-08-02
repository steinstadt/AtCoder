# Problem C - Repsept
# input
K = int(input())

# initialization
seven = 7
ans = 1

# count
if K%2==0 or K%5==0:
    ans = -1
elif K==1:
    ans = 1
else:
    tmp_list = [0]*(10**6+1)
    while not seven%K==0: # 割り切れない限り
        seven = seven*10 + 7
        seven = seven % K
        ans += 1


# output
print(ans)
