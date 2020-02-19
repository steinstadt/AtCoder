S = input()
num_cnt = len(S)
op_cnt = len(S) - 1  # すき間の個数
ope_sum = 0
for i in range(2 ** op_cnt):
    op = [""] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"  # フラグが立っていた箇所を "+" で上書き

    formula = ""
    for j in range(num_cnt):
        if j==num_cnt-1:
            formula = formula + S[j]
            ope_sum = ope_sum + eval(formula)
            break
        formula = formula + S[j] + op[j]

print(ope_sum)
