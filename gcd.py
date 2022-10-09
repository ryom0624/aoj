x, y = map(int, input().split())
if x < y: x,y = y,x
a = 0
a = x%y
if(a == 0):
    print(y)
    exit()

while(True):
    b = y%a
    if b == 0:
        print(a)
        exit()
    else:
        y = a
        a = b
