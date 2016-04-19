n=int(input("Nhap vao mot so( lon hon 1): "))
i=0

while 1<i<n:
    s=n%i
    i=i+1
if s==0:
    print(str.format("{0} la so nguyen to",n))
else:
    print(str.format("{0} khong phai la so nguyen to",n))
