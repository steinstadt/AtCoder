# Problem D - Double Dots

from collections import deque

# input
N, M = map(int, input().split())
graph_list = {}
for i in range(M):
    a, b = map(int, input().split())
    if a in graph_list:
        graph_list[a].append(b)
    else:
        graph_list[a] = [b]

    if b in graph_list:
        graph_list[b].append(a)
    else:
        graph_list[b] = [a]

# initialization
visit_list = [0]*N
distance_list = [float("INF")]*N
distance_list[0] = 0
visit_queue = deque([1])
queue_count = 1

# bfs search
while queue_count>0:
    v = visit_queue.popleft()
    queue_count -= 1

    graph = graph_list[v]
    for n in graph:
        if distance_list[v-1]+1<distance_list[n-1]:
            distance_list[n-1] = distance_list[v-1] + 1
            visit_list[n-1] = v
            visit_queue.append(n)
            queue_count += 1

# output
print("Yes")
for i in range(1, N):
    print(visit_list[i])
