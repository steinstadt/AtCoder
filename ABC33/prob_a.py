# Problem A - 暗証番号

# input
N = list(input())

# initialization
nums_len = len(set(N))

# output
if nums_len==1:
    print("SAME")
else:
    print("DIFFERENT")
