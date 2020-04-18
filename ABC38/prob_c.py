# Problem C - 単調増加

# input
N = int(input())
a_list = list(map(int, input().split()))

# initialization
ans = 0

# shakutori count
right = 0
for left in range(N):
    while (right<N and a_list[right-1]<a_list[right]) or left==right:
        right += 1

    ans += right - left

    if left==right:
        right += 1

# output
print(ans)
