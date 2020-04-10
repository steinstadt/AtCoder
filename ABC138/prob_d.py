# Problem D - Ki

# input
N, Q = map(int, input().split())
tree_list = {}
for i in range(N):
    tree_list[i+1] = []
for i in range(N-1):
    a, b = map(int, input().split())
    tree_list[a].append(b)
cost_list = [0]*N

# cost check
for i in range(Q):
    p, x = map(int, input().split())
    cost_list[p-1] += x

# search
search_queue = []
search_queue.append(1)
while len(search_queue)>0:
    q = search_queue.pop()
    childs = tree_list[q]
    if len(childs)<=0:
        continue
    for c in childs:
        cost_list[c-1] += cost_list[q-1]
        search_queue.append(c)

# output
print(" ".join(list(map(str,cost_list))))
