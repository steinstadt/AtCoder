# Problem A - Pair

K = int(input())
odd_list = []
even_list = []

for k in range(1, K+1):
    if k%2==0:
        even_list.append(k)
    else:
        odd_list.append(k)

print(len(odd_list)*len(even_list))
