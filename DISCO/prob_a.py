# Problem A - DDCC Finals

# input process
X, Y = map(int, input().split())

# initialization
cost_ans = 0

if X==1:
    cost_ans += 300000
elif X==2:
    cost_ans += 200000
elif X==3:
    cost_ans += 100000

if Y==1:
    cost_ans += 300000
elif Y==2:
    cost_ans += 200000
elif Y==3:
    cost_ans += 100000

if X==1 and Y==1:
    cost_ans += 400000

print(cost_ans)
