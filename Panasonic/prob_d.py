# Problem D - String Equivalence

from collections import deque

# input
N = int(input())

char_list = [chr(i) for i in range(97, 97+26)]

def dfs(a_list, a_len):
    if a_len==N:
        print("".join(a_list))
        return
    else:
        biggest = 97
        count = len(set(a_list)) # N<=10だからさほど時間はかからない
        for c in range(biggest, biggest + count + 1):
            ch = chr(c)
            a_list.append(ch)
            dfs(a_list, a_len+1)
            a_list.pop()

# initialization
a_nums = deque([])

# dfs search
dfs(a_nums, 0)
