# Problem A - Study Scheduling

# input
h_1, m_1, h_2, m_2, k = map(int, input().split())

# initialization
if m_2-k>=0:
    m_2 -= k
else:
    tmp = k - m_2
    m_2 = 60 - tmp
    h_2 -= 1
tmp_1 = h_1 * 60 + m_1
tmp_2 = h_2 * 60 + m_2

# calc
ans = tmp_2 - tmp_1

# output
print(ans)
