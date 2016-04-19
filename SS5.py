from turtle import*
import random
def draw_triangle(x,y,length):	#tu khoa def (ten_ham) (tham so):
    penup()
    goto(x,y)
    pendown()			#than ham: ve hinh tam giac co chieu dai
    fd(length)				 #  nhat dinh tai mot diem x, y bat ki
    lt(120)
    fd(length)
    lt(120)
    fd(length)
draw_triangle(5,50,250)		#minh goi ham ra va nhap tham so vao
draw_triangle(45,45,250)
speed(0)			#cai nay la de con turtle ve nhanh hon thoi
i=0
while i<100:
    x= random.randint(-100,100)		# doan nay la ve 100 cai tam giac bat ki 
    y= random.randint(-100,100)		# o vi tri ngau nhien su dung ham random
    length= random.randint(-10,100)
    draw_triangle(x,y,length)
    i=i+1
    

