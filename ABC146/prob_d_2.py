from collections import deque

n=int(input())
G=[[]for _ in range(n)]
L=[]
ans=[0]*n
for i in range(n-1):
   a,b=map(int,input().split())
   G[a-1].append(b-1)
   L.append(b-1)

que=deque([0])
while que:
   s=que.pop()
   color=1
   for ni in G[s]:
      if ans[s]==color:
         color+=1
      ans[ni]=color
      color+=1
      que.append(ni)
print(max(ans))
for i in L:
   print(ans[i])
