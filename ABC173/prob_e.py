n,k=map(int,input().split())
A=[int(i) for i in input().split()]
A.sort(key=lambda x:-abs(x))
mod=10**9+7

ans=1
if (max(A)<=0 and k%2==1) or n==k:
    for i in range(k):
        ans=ans*A[n-1-i]%mod
else:
    mi=0
    pl=0
    flg=1
    for i in range(k):
        ans=ans*A[i]%mod
        if A[i]>0:
            pl=A[i]
        if A[i]<0:
            mi=A[i]
            flg*=-1
    if ans==0:
        pass
    elif flg==-1:
        mi2=None
        pl2=None
        for i in range(k,n):
            if A[i]>=0:
                pl2=A[i]
                break
        for i in range(k,n):
            if A[i]<=0:
                mi2=A[i]
                break
        can=0
        if mi!=0 and pl2 is not None and pl!=0 and mi2 is not None:
            if pl2*pl > mi2*mi:
                can = pow(mi,-1,mod)*pl2%mod
            else:
                can = pow(pl,-1,mod)*mi2%mod
        elif mi!=0 and pl2 is not None:
            can = pow(mi,-1,mod)*pl2%mod
        elif pl!=0 and mi2 is not None:
            can = pow(pl,-1,mod)*mi2%mod
        ans=ans*can%mod

print(ans)
