import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
p=(a+b+c)/2
if a>0 and b>0 and c>0:
    if (a+b)>c and (a+c)>b and (b+c)>a:
        print('Dien tich=',round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3), sep='')
    else:
        print('Khong hop le')
else:
    print('Khong hop le')