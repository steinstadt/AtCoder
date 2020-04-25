# Problem D - Coloring Edges on Tree

from collections import deque

# input
N = int(input())
node_list = {} # 隣接リストの作成
color_count_list = [0]*(N+1)
ans_list = []
for i in range(N-1):
    a, b = map(int, input().split())
    if a in node_list:
        node_list[a].append(b)
    else:
        node_list[a] = [b]
    color_count_list[a] += 1
    color_count_list[b] += 1
    ans_list.append([a, b])

# initialization
color_list = {}
color_max_count = max(color_count_list)

# bfs search
visit_queue = deque([[-1, 1]]) # [[既に使った色], 遷移ノード]
while len(visit_queue)>0:
    p = visit_queue.popleft()

    used_color = p[0]
    if p[1] in node_list:
        nodes = node_list[p[1]]
        nodes_len = len(nodes)
        color_num = 1
        if nodes_len>=1:
            coloring_count = 0
            while coloring_count<nodes_len:
                if color_num==used_color:
                    color_num += 1
                    continue
                # 隣接リストによる表現
                if p[1] in color_list:
                    color_list[p[1]][nodes[coloring_count]] = color_num
                else:
                    color_list[p[1]] = {nodes[coloring_count]:color_num}
                if nodes[coloring_count] in color_list:
                    color_list[nodes[coloring_count]][p[1]] = color_num
                else:
                    color_list[nodes[coloring_count]] = {p[1]:color_num}
                # queue insert
                visit_queue.append([color_num, nodes[coloring_count]])
                # color update
                coloring_count += 1
                color_num += 1

# output
print(color_max_count)
for a in ans_list:
    print(color_list[a[0]][a[1]])
