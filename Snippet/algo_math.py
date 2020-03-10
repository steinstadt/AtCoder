# 競技プログラミングで使える関数集合

# 最大公約数を列挙する関数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

# bit全探索を行ってくれる関数
def bit_search():
    opt_list = []
    for i in range(8):
        opt = [0, 0, 0]
        for j in range(3):
            if ((i>>j)&1):
                opt[3-j-1] = 1
        opt_list.append(opt)
