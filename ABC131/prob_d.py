# Problem D - Megalomania

# input
N = int(input())

# initialization
cost_list = []
for i in range(N):
    A, B = map(int, input().split())
    cost_list.append([A, B])
cost_list.sort(key=lambda x: x[1])
time_cost = 0

# time count
is_ok = True
for c in cost_list:
    A = c[0]
    B = c[1]
    time_cost += A
    if time_cost>B:
        is_ok = False
        break

# output
if is_ok:
    print("Yes")
else:
    print("No")
