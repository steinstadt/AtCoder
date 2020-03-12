# Problem A - Colorful Slimes 2

# input process
N = int(input())
a_list = list(map(int, input().split()))

# initialization
even_count = 0
odd_count = 0

# count process
for i in range(N):
    if i%2==0: # odd count
        if i-1>=0:
            if a_list[i]==a_list[i-1]:
                odd_count += 1
                continue
        if i+1<N:
            if a_list[i]==a_list[i+1]:
                odd_count += 1
    else: # even count
        if i-1>=0:
            if a_list[i]==a_list[i-1]:
                even_count += 1
                continue
        if i+1<N:
            if a_list[i]==a_list[i+1]:
                even_count += 1

ans = min(even_count, odd_count)
print(ans)
