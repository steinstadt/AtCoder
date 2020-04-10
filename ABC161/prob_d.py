# Problem D - Lunlun Number

from collections import deque

# input
K = int(input())

# initialization
num_queue = deque()
k = 1

# count
while True:
    if k>=1 and k<=9:
        num_queue.append(k)
        k += 1
    else:
        num = str(num_queue.popleft())
        num_str = int(num[-1])
        if num_str==0:
            for i in range(2):
                tmp = str(i)
                num_queue.append(int(num + tmp))
                k += 1
                if k-1==K:
                    break
        elif num_str==9:
            for i in range(8,10):
                tmp = str(i)
                num_queue.append(int(num + tmp))
                k += 1
                if k-1==K:
                    break
        else:
            for i in range(num_str-1, num_str+2):
                tmp = str(i)
                num_queue.append(int(num + tmp))
                k += 1
                if k-1==K:
                    break

    if k-1==K:
        break

# output
print(num_queue[-1])
