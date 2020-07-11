# Problem B - Judge Status Summary

# input
N = int(input())

# initialization
ac = 0
wa = 0
tle = 0
re = 0

# count
for i in range(N):
    s = input()

    if s=='AC':
        ac += 1
    elif s=='WA':
        wa += 1
    elif s=='TLE':
        tle += 1
    else:
        re += 1

# output
print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))
