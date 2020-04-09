# Problem C - Train Ticket

# input
ABCD = input()
A = ABCD[0]
B = ABCD[1]
C = ABCD[2]
D = ABCD[3]

# initialization
pattern_list = []
for i in range(2**3):
    p = ['-']*3
    for j in range(3):
        if (i>>j)&1:
            p[j] = '+'
    pattern_list.append(p)

# check loop
for p in pattern_list:
    calc_str = A + p[0] + B + p[1] + C + p[2] + D
    if eval(calc_str)==7:
        calc_str += '=7'
        print(calc_str)
        break
