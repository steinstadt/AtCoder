# Problem C - Guess The Number

# input
N, M = map(int, input().split())

# initialization
keta = 0
if N==0:
    keta = 1
else:
    keta = N
keta_list = [-1]*keta
input_ok = True
for i in range(M):
    s, c = map(int, input().split())
    if not keta_list[s-1]==-1:
        if not keta_list[s-1]==c:
            input_ok = False
            break
    else:
        keta_list[s-1] = c
if keta>1 and keta_list[0]==0:
    input_ok = False

if input_ok:
    if keta==1:
        if keta_list[0]==-1:
            print(0)
        else:
            print(keta_list[0])
    else:
        ans = 100000
        for n in range(1000):
            tmp_keta = len(str(n))
            if tmp_keta==keta:
                tmp = ''
                for i in range(len(keta_list)):
                    if i==0 and keta_list[i]==-1:
                        tmp += '1'
                    elif keta_list[i]==-1:
                        tmp += '0'
                    else:
                        tmp += str(keta_list[i])
                tmp = int(tmp)
                ans = min(ans, tmp)
        print(ans)
else:
    print(-1)
