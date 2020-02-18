N = int(input())
a_list = list(map(int, input().split()))

odd_count = 0
for i in range(N):
    if not a_list[i]%2==0:
        odd_count = odd_count + 1

if odd_count%2==0:
    print("Yes")
else:
    print("No")
