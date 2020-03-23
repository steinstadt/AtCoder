# Problem A - スーパーICT高校生

# input process
S = input()

# initialization
teacher_data = 'ict '
str_step = 0

# step process
for i in range(len(S)):
    if S[i].lower()==teacher_data[str_step]:
        str_step += 1

    if str_step==3:
        break

# output process
if str_step==3:
    print('YES')
else:
    print('NO')
