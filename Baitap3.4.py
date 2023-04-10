Toan=float(input())
Ly=float(input())
Hoa=float(input())
Tb=(Toan*2+Ly*3+Hoa)/6
if Tb<3:
    print('Kem')
elif Tb>=3 and Tb<5:
    print('Yeu')
elif Tb>=5 and Tb<6:
    print('Trung binh')
elif Tb>=6 and Tb<7:
    print('Trung binh kha')
elif Tb>=7 and Tb<8:
    print('Kha')
elif Tb>=8 and Tb<9:
    print('Gioi')
elif Tb>=9 and Tb<10:
    print('Xuat sac')