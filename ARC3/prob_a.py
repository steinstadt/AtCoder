# Problem A - GPA計算

# input process
N = int(input())
r_list = input()

# initialization
f_count = 0
ans_score = 0

for i in range(N):
    r = r_list[i]

    if r=="A":
        ans_score = ans_score + 4
    elif r=="B":
        ans_score = ans_score + 3
    elif r=="C":
        ans_score = ans_score + 2
    elif r=="D":
        ans_score = ans_score + 1
    elif r=="F":
        f_count = f_count + 1

if f_count==N:
    print(0)
else:
    print(ans_score/N)
