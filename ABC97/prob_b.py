X = int(input())

X_half = X // 2
max_ans = 1
tmp_max = 0

for i in range(1,X_half+10):
    for j in range(2,X_half+10):
        tmp = i ** j
        if tmp<=X:
            tmp_max = tmp
    max_ans = max(max_ans, tmp_max)

print(max_ans)
