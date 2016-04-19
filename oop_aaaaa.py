##class person:
##    def __init__(self):   #def __init__(self,a,n)
##        self.name = ""    #self.name=a
##        self.age = -1     #self.age=n
##    def display(self):
##        print("Name: ",self.name)
##        print("Age: ",self.age)
##        
##
##p=person() ## toi muon khai bao 1 valible p giong 1 doi tuong person, p la 1 ngoi nha rong chua co gi _init_ la 1 ham tao
##p.name = "son dep trai"
##p.age = 100
###c1111111111
##print("Name":p.name)
##print("Age" : p.age)
###c2222222
##p.display()
##### open smtp gmail
import smtplib
user_name = "c4e3.techkids"
password = "xanhgimaxanhthe"
from_addr="quyendaptrai@gmail.com"
to_addr= "hiepxanh@gmail.com"
server=smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(user_name, password)
server.sendmail(from_addr,to_addr,"Subject: Hiep oi\nCho nao cua anh xanh vay, cho em xem")
server.close()
#### open csv
