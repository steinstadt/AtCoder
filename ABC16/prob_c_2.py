# Problem C - 友達の友達

# input
N, M = map(int, input().split())
graph_list = {}
for i in range(N):
    graph_list[i+1] = []
for i in range(M):
    A, B = map(int, input().split())
    graph_list[A].append(B)
    graph_list[B].append(A)


# friends search
for g in graph_list:
    friends_count = 0
    friends = graph_list[g]
    # friend friend search
    for f in friends:
        friend_friend = graph_list[f]
        for ff in friend_friend:
            if ff==g:
                continue
            f_friends = graph_list[ff]
            for fff in f_friends:
                if not fff==g:
                    friends_count += 1
                else:
                    friends_count = 0
                    break
    # output
    print(friends_count)
