# Problem C - String Transformation

# input
S = list(input())
T = list(input())

# initialization
s_map = {}
t_map = {}
is_ok = True

# mapping
for i in range(len(S)):
    s = S[i]
    t = T[i]
    if not s in s_map:
        s_map[s] = set([t])
    else:
        s_map[s].add(t)

    if not t in t_map:
        t_map[t] = set([s])
    else:
        t_map[t].add(s)

# check
# s check
for s in s_map:
    if len(s_map[s])>1:
        is_ok = False
# t check
for t in t_map:
    if len(t_map[t])>1:
        is_ok = False

# output
if is_ok:
    print("Yes")
else:
    print("No")
