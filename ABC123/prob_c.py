import math

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

t_list = [A, B, C, D, E]
min_t = min(t_list)
min_i = 0

t_1 = math.ceil(N/min_t)
t_1 = int((N+min_t-1) / min_t)
print(t_1+4)
