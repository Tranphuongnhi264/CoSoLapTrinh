Ten=input('Ho ten: ')
SoCong=int(input('So ngay cong: '))
DonGia=float(input('Don gia ngay cong: '))
HeSo=float(input('He so phu cap: '))
Ung=int(input('Tam ung: '))
a=DonGia*SoCong*HeSo
print('Nhan vien ',Ten,', Co tien Luong=',round(a,1),', Tam ung=',Ung,sep='',end='')
print(' va Thuc linh=',round(a-Ung,1),sep='')