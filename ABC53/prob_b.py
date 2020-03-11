# Problem B - A to Z String

# input process
s = input()
s_len = len(s)

# initizalization
a_pos = 0
z_pos = 0

# first a search
for i in range(s_len):
    a = s[i]
    if a=='A':
        a_pos = i
        break

# second z search
for i in range(s_len):
    z = s[i]
    if z=='Z':
        z_pos = i

print(z_pos - a_pos + 1)
