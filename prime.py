n=int(input("Nhap vao mot so: "))
i=2
if n >=1:
    while i<(n-1):
        if(n % i)==0:
            print(n,"is not prime number")
            break
        i=i+1
    else:
        print(n,"is a prime number")

