# Problem B - Small and Large Integers

A, B, K = map(int, input().split())

# initialization

if B-A<=2*K:
    num_list = [i for i in range(A,B+1)]
    # output process 1
    for i in range(K):
        if len(num_list)<=0:
            break
        n = num_list[0]
        print(n)
        num_list.remove(n)

    # output process 2
    output_list = []
    for i in range(K):
        if len(num_list)<=0:
            break
        n = num_list[-1]
        output_list.append(n)
        num_list.remove(n)

    output_list = output_list[::-1]

    for o in output_list:
        print(o)
else:
    num_list_1 = [i for i in range(A, A+K+1)]
    num_list_2 = [i for i in range(B-K+1, B+1)]
    # output process 1
    for i in range(K):
        n = num_list_1[i]
        print(n)

    # output process 2
    for i in range(K):
        n = num_list_2[i]
        print(n)
