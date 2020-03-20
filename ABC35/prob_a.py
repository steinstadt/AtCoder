# Problem A - テレビ

# input porcess
w, h = map(int, input().split())

# initialization
aspect_rate_1 = 3 / 4
aspect_rate_2 = 9 / 16

# check process
if h/w == aspect_rate_1:
    print("4:3")
elif h/w == aspect_rate_2:
    print("16:9")
else:
    print("Nothing")
    
