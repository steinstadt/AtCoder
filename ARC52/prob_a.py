# Problem A - 何期生？
import re

# input process
S = input()

# initialization
num_str = ''

# search process
pattern = '\d+'
ans = re.search(pattern, S)

# output process
print(ans.group())
