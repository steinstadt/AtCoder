# Problem A - Therefore
# input
n = int(list(input())[-1])

# initialization
yomi = list('pphbhhphph')

# output
ans = yomi[n]
if ans=='p':
    print('pon')
elif ans=='b':
    print('bon')
else:
    print('hon')
