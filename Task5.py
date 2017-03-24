def triangle(a, b, c): 
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        f = True
    else:
        f = False
    return f
a = input("a = ")
a = int(a)
b = input("b = ")
b = int(b)
c = input("c = ")
c = int(c)
print(triangle(a, b, c))
