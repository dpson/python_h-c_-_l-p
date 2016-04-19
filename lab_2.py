###hanh dong lap di lap lai
##for name in "Linh", "Thao","Minh":
##    print("Hello " + name)
##    
##for n in "5", "7", "11", "3":
##    print(""+ n)
# wavu 3
##for i in range(0,1000):
##    print("Anh Yeu Em!!!")
##print("Anh Yeu em 1001 lan roi nhe")
######## wave 6
##list = "chua bao gio", " de em roi xa", "Tam Su Voi Nguoi La"
##print("My playlist is: ")
##for a in range(3):
##    print(str.format("{0}: {1}",a,list[a]))
##n=input("enter song name here: ")
##n=n.lower()
##for name in list:
##    if n==name:
##        print("Play")
##        break
##    else:
##        print("Not play")
##        break
#C2 if n in list:
##      print("play")
##    else:
##      print("not play")
################WAV1 DRAW
##from turtle import *
##def draw(list):
##    list= "tam giac", "tu giac", "ngu giac"
##    for n in range(3):
##        m=input("tam giac or tu giac or ngu giac: ")
##        if m==list[n]:
##            while n<n+2:
##                forward(50)
##                left(360/(n+3))
##
##        else:
##            print("Khong co hinh nao can ve: ")
##a=draw(list)
##        
   
##########Wave 2:old friend
##from turtle import *
##def baba(x):
##    for x in range(0,x):
##      forward(20)
##      penup()
##      forward(10)
##      pendown()
##      forward(20+x)
##m=int(input("SO loop: "))
##a=baba(m)
########hexagon
##from turtle import *
##def hexagon():
##   for n in range(0,6):
##       forward(50)
##       left(60)
##i=0
##while i<6:
##   hexagon()
##   forward(50)
##   right(60)
##   
##   
##   i=i+1
######## ord chuyen ki tu thanh so
list="abc"
s=""
for i in list:
    x=ord(i) ##3 chuyen x thanh so
    s.append(x)
    print(s,end=" ")

       

   
