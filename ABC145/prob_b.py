# Problem B - Echo

# input process
N = int(input())
S = input()

if not N%2==0:
    print('No')
else:
    parts_1 = S[:(N//2)]
    parts_2 = S[N//2:]
    if parts_1==parts_2:
        print('Yes')
    else:
        print('No')
