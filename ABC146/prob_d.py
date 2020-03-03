# input process
N = int(input())
graph_list = {}
graph_parent_list = {}
visit_list = {}

# initialization
for i in range(N):
    graph_list[i+1] = []
    graph_parent_list[i+1] = {}

for i in range(N-1):
    a, b = map(int, input().split())
    graph_list[a].append(b) # edge state settings
    graph_list[b].append(a)
    graph_parent_list[b][a] = 0 # edge parent settings <- color info

max_ans = 0
# max ans process
for g_key in graph_list:
    max_ans = max(max_ans, len(graph_list[g_key]))

# breadth first search
edge_list = [i for i in range(1, max_ans+1)]
color_list = []
root = 1
search_queue = []
search_queue.append([root,graph_list[root]])
while len(search_queue)>0:
    tmp_edge = [i for i in range(1, max_ans+1)]
    s_in = search_queue.pop() # [1, [2]], [2, [1, 3, 4, 5]]
    s_num = s_in[0] # 1, 2
    s_list = s_in[1] # [2], [1, 3, 4, 5]
    # parent cut process
    if s_num in graph_parent_list:
        for e_key in graph_parent_list[s_num]:
            tmp_edge.remove(graph_parent_list[s_num][e_key])
            s_list.remove(e_key)
    # visited node search
    for i in range(len(s_list)):
        c = tmp_edge[i]
        s = s_list[i]
        color_list.append(c) # color output
        graph_parent_list[s][s_num] = c
        search_queue.append([s, graph_list[s]]) # search queue insert


# output process
print(max_ans)
for c in color_list:
    print(c)
