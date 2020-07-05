# Problem D - Teleporter

# input
N, K = map(int, input().split())
a_list = list(map(int, input().split()))

# initialization
visit_list = [0] * N
pos = a_list[0]
visit_list[pos-1] = 1
visit_count = 1
remain = K - 1
is_ok = True
ans = 0

# count
while remain>0 and is_ok:
    pos = a_list[pos-1]
    remain -= 1
    visit_count += 1
    if pos==1 or not visit_list[pos-1]==0:
        tmp_1 = visit_count - visit_list[pos-1]
        tmp_2 = remain % tmp_1
        for t in range(tmp_2):
            pos = a_list[pos-1]
        is_ok = False
        break
    else:
        visit_list[pos-1] = visit_count

# output
print(pos)
