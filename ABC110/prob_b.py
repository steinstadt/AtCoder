# Problem B - 1 Dimensional World's Tale

# input
N, M, X, Y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

# initialization
is_ok = True
x_koho = [X]
y_koho = [Y]

# x select
for x in x_list:
    if x>=X:
        x_koho.append(x)

# y select
for y in y_list:
    if y<=Y:
        y_koho.append(y)

x_max = max(x_koho)
y_min = min(y_koho)

# output
if y_min-x_max>0:
    print("No War")
else:
    print("War")
