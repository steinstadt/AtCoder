# Problem B - Contests

# input process
N = int(input())
A, B = map(int, input().split())
P_list = list(map(int, input().split()))

# initizaliation
combi_1 = []
combi_2 = []
combi_3 = []

# count step
for p in P_list:
    if p<=A:
        combi_1.append(p)
    elif p>=(A+1) and p<=B:
        combi_2.append(p)
    else:
        combi_3.append(p)

# output process
ans = min(len(combi_1), len(combi_2), len(combi_3))
print(ans)
