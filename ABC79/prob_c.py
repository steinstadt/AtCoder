# Problem C - Train Ticket ビット全探索の問題

# input process
Num = input()
ABCD = [Num[0], Num[1], Num[2], Num[3]]

# initialization
opt_list = []
for i in range(8):
    opt = [0, 0, 0]
    for j in range(3):
        if ((i>>j)&1):
            opt[3-j-1] = 1
    opt_list.append(opt)

# bit search start
for opt in opt_list:
    math_formula = ""
    for i in range(3):
        if opt[i]==1:
            math_formula += ABCD[i] + "+"
        else:
            math_formula += ABCD[i] + "-"
    math_formula += ABCD[3]
    if eval(math_formula)==7:
        print(math_formula+"=7")
        break
