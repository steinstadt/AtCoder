# 双子とスイカ割り

def limit_num(n, a, b):
    if n<=a:
        return a
    elif n>=b:
        return b
    else:
        return n

# input process
N, A, B = map(int, input().split())

# initialization
current_pos = 0

# count process
for i in range(N):
    s, d = input().split()
    d = int(d)
    d = limit_num(d, A, B)
    if s=='East':
        current_pos -= d
    else:
        current_pos += d

# output process
if current_pos>0:
    print("West %d"%(current_pos))
elif current_pos<0:
    print("East %d"%(abs(current_pos)))
else:
    print(0)
