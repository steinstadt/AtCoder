# Problem B - Lucas Number

# input
N = int(input())

# initialization
lucas = [0]*100

# count
for i in range(N+1):
    if i==0:
        lucas[i] = 2
    elif i==1:
        lucas[i] = 1
    else:
        lucas[i] = lucas[i-1] + lucas[i-2]

# output
print(lucas[N])
