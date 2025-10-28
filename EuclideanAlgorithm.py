def f(a,b):
    if b==0:
        return (a, 1, 0)
    else:
        d, x1, y1 = f(b, a%b)
        d, x, y = d, y1, x1 - (a//b)*y1
        return (d, x, y)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
d, x, y=f(a,b)
print(a, "* (", x, ") + ", b, "* (", y, ") = ", d)
