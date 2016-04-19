
##
##while y<3:
##    n=input("what your name?")
##    if n== "dac":
##        print("hello handsome dac")
##    elif n =="thao":
##        print("Hello pretty thao")
##    else:    
##
##        print("Hello",n)
##    
##    #yob= int (input ("what your year of birth?"))
##
##    #print(2016-yob)
##
##
##    print("Hello World")
##    y=y+1;
while True: 
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    delta=b**2 - 4*a*c
    
    
    if delta < 0 :
        print("Phuong trinh vo nghiem")
    elif delta==0:
        x=(-b)/(2*a)
        print("Phuong trinh co nghiem kep x =",x)
    else:
        x1=(-b+delta**0.5)/(2*a)
        x2=(-b-delta**0.5)/(2*a)
        print ("Phuong trinh co 2 nghiem")
        print ("x1=",x1)
        print ("x2=",x2)
