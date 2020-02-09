import re

N = int(input())
K = int(input())

count = 0

for num in range(1,N+1):
    num_str = str(num)
    num_str = re.sub("0", "", num_str)
    str_num = int(num_str)
    str_len = len(num_str)
    if str_num <= num and str_len==K:
        count = count + 1
    elif str_num <= 10 and str_len==K:
        count = count + 1

print(count)
