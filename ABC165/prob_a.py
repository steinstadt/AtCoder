K = int(input())
A, B = map(int, input().split())

# initialization
is_ok = False

for i in range(A, B+1):
    if i%K==0:
        is_ok = True
        break

# output
if is_ok:
    print("OK")
else:
    print("NG")
