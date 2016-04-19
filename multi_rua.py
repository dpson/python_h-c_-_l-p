from turtle import*
import webbrowser
import time
import datetime
time.clock_settime(m, 20)
i=0
if m>=20 and m<=21:
    time.sleep(30)
    color('red','white')
    begin_fill()
    while i<5:
        circle(50)
        right(60)
        circle(50)
        i=i+1
    webbrowser.open("youtube.com")
elif m>21 and m<=22:
    time.sleep(30)
    color('yellow','white')
    begin_fill()
    while i<24:
        circle(100)
        right(15)
        circle(100)
        i=i+1
    webbrowser.open("google.com")
    
