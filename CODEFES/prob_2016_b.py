# Problem B -Qualification simulator

# input
N, A, B = map(int, input().split())
S = list(input())

# initialization
rank_num = 0
rank_b_num = 0

# score roop
for s in S:
    if s=='a':
        if rank_num<A+B:
            print("Yes")
            rank_num += 1
        else:
            print("No")
    elif s=='c':
        print("No")
    elif s=='b':
        if rank_num<A+B and rank_b_num<B:
            print("Yes")
            rank_num += 1
            rank_b_num += 1
        else:
            print("No")
