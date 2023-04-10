M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S='))
if S<= 100:
    print('Phai tra=',S*M1, sep='')
elif S>=101 and S<= 150:
    print('Phai tra=',S*M2,sep='')
elif S>=151:
    print('Phai tra=',S*M3,sep='')