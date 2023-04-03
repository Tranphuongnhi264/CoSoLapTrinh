import math
print('Nhap hai canh ke cua tam giac vuong:')
a=float(input())
b=float(input())
a=int(a); b=int(b)
print('Canh ke thu nhat la:',str(a)+', canh ke thu hai:',b,end='')
print(', co canh huyen =',round(math.sqrt(a*a+b*b), 2))