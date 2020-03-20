# Problem B - Collatz Problem

# input process
s = int(input())
min_m = 1
number_queue = []
number_queue.append(s)

# search process
while True:
    min_m += 1
    if s%2==0:
        s = s / 2
    else:
        s = 3 * s + 1

    if s in number_queue:
        break

    number_queue.append(s)

# output process
print(min_m)
