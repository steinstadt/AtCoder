# KEYENCE String 全通りのパターンを探索する

# input process
S = input()
s_length = len(S)

# initialization
is_same = False
for i in range(s_length):
    for j in range(i, s_length):
        # string slice
        tmp_str = S[:i+1] + S[j:]
        if tmp_str=="keyence":
            is_same = True
            break

# 出力方法に気をつけて！　YesとYESの違いでWrong Answerがでた
if is_same:
    print("YES")
else:
    print("NO")
