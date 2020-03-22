# Problem A - お茶
import math

# input
a, b = map(int, input().split())

# initialization
box_count = 0

# count
box_count = math.ceil(b / a)

# output
print(box_count)
