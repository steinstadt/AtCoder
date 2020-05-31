# Problem D - Double Dots

from collections import deque

# input
N, M = map(int, input().split())

# initialization
nodes = [0] * N
visit = [0] * N
edges_dic = {}
for i in range(M):
    A, B = map(int, input().split())
    if A in edges_dic:
        edges_dic[A].append(B)
    else:
        edges_dic[A] = [B]

    if B in edges_dic:
        edges_dic[B].append(A)
    else:
        edges_dic[B] = [A]
queue = deque([1])

# search
while len(queue)>=1:
    q = queue.popleft()
    visit[q-1] = 1
    next_n = edges_dic[q]
    for n in next_n:
        if visit[n-1]==0:
            nodes[n-1] = q
            visit[n-1] = 1
            queue.append(n)

# output
print("Yes")
for i in range(1, N):
    print(nodes[i])
