def distance(x1, x2, y1, y2):
    res = ((x1-x2)**2+(y1-y2)**2)**1/2
    return res
x1 = input("x1 = ")
x1 = float(x1)
x2 = input("x2 = ")
x2 = float(x2)
y1 = input("y1 = ")
y1 = float(y1)
y2 = input("y2 = ")
y2 = float(y2)
print(distance(x1, x2, y1, y2))
