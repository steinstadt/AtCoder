# Problem A - Meal Delivery
# input
x, a, b = map(int, input().split())

# check
if abs(x-b)>abs(x-a):
    print("A")
else:
    print("B")
