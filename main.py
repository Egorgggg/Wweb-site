from math import sqrt
def f(x):
    return -x**2 + 4

def fp(a,b):
    return abs((f(a) + f(b))/2 * (a-b))

def L(a,b):
    return sqrt((f(b)-f(a))**2 + (b-a)**2)

a = -2
b = 2
n = 100
h = (abs(a)+abs(b))/n
s = 0
l = 0
for  i in range(0,n):
    s += fp(a + i*h,a + (i+1)*h)
    l += abs(L(a+i*h,a + (i+1)*h))

print(s)
print(l)      