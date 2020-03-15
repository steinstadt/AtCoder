# Problem C - Sqrt Inequality

# 注意：ルートの計算は近似計算によりWAとなってしまう。
#    ：整数に落とし込んで計算しよう

# input process
a, b, c = map(int, input().split())

# initialization
tochu_1 = c - a - b
tochu_2 = 4 * a * b

# output process
if tochu_1>0 and (tochu_1)**2>tochu_2:
    print("Yes")
else:
    print("No")
