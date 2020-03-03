N, M = map(int, input().split())
if M==0:
    keta = ['0']*N
    if N!=1:
        keta[0]=1
        ans = ""
        for i in range(len(keta)):
            ans = ans + str(keta[i])
        ans = int(ans)
        print(ans)
    else:
        print(keta[0][0])
else:
    keta_list = [[-1]*(N) for i in range(M)]
    b_ans = True

    #initialization
    s, c = map(int, input().split())
    keta_list[0][s-1] = c

    for i in range(M-1):
        s_t, c_t = map(int, input().split())
        s_t = s_t - 1
        if keta_list[i][s_t] == -1:
            keta_list[i][s_t] = c_t
            for j in range(i,M-1):
                for k in range(N):
                    keta_list[j+1][k] = keta_list[j][k]
        elif keta_list[i][s_t]!=c_t:
            b_ans = False
            break
        else: # same num
            for j in range(i,M-1):
                for k in range(N):
                    keta_list[j+1][k] = keta_list[j][k]

    if b_ans:
        # list search
        ans_list = keta_list[M-1]
        for i in range(len(ans_list)):
            if ans_list[i]==-1:
                ans_list[i] = 0
        # sentou shori
        if ans_list[0]==0:
            print(-1)
        else:
            ans = ""
            for a in ans_list:
                ans = ans + str(a)
            ans = int(ans)
            print(ans)
    else:
        print(-1)
