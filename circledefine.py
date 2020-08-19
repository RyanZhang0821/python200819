def circle_area(x):
    num=x*x*3.14
    return num

def circle_circum(x):
    num=x*2*3.14
    return num
n=int(input('半徑:'))
n=circle_area(n)
print(n)
n=int(input('半徑:'))
n=circle_circum(n)
print(n)