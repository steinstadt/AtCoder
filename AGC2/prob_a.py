# Problem A - Range Product
# input
a, b = map(int, input().split())

# calc
if (a==0 or b==0) or (a<0 and b>0) or (a>0 and b<0):
    print("Zero")
elif a>0 and b>0:
    print("Positive")
elif a<0 and b<0:
    nums = abs(b - a) + 1
    if nums%2==1:
        print("Negative")
    else:
        print("Positive")
