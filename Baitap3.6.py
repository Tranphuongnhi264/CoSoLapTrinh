a=float(input())
b=float(input())
c=float(input())
if a>0 and b>0 and c>0:
    if (a+b)>c and (a+c)>b and(b+c)>a:
        if (a*a== b*b+c*c)or(b*b==c*c+a*a)or(c*c==b*b+a*a):
            print('Tam giac vuong')
        elif (a==b) and(b==c) and(a==c):
            print('Tam giac deu')
        else:
            print('Tam giac loai khac')
    else:
        print('Khong hop le')        
else:
    print('Khong hop le')