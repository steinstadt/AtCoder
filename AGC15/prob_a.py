# Problem A - A+...+B Problem

# input
N, A, B = map(int, input().split())

# corner case
if A>B:
    print(0)
elif N==1 and A!=B:
    print(0)
elif N==1 and A==B:
    print(1)
else:
    ans = (N-2)*(B-A) + 1
    print(ans)
