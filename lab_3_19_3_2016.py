# -*- coding: utf-8-*-
from pymongo import MongoClient

URI = "mongodb://c4e3:codethechange@ds015869.mlab.com:15869/c4e3_son_movie"
client = MongoClient(URI)
db = client.get_default_database()
account = db["son"]
##def insert(name,so_buoi_day,luong_buoi):
    
##   
##    result = account.insert_one(
##        {
##        
##                "STT" : "1",
##                "Tên" : name,
##                "Team": "C4E3",
##                "Lop": "C4E3",
##                "Sô Buôi day" : so_buoi_day,
##                "Luong/Buoi" : luong_buoi,
##        }
##        )
##    print(result)
##while True:
##    Ten=input("Nhap vao ten giang vien: ")
##    a = input("Nhap vao so buoi day: ")
##    b= input("Luong/buoi: ")
##    insert(Ten,a,b)
#########find name            
##def find(name):
##        
##        mama=account.find()
##        for name in mama:
##            print(name)
##        
##ten = input("Nhap vao giang vien can tim: ")
##find(ten)
########## wave 3: update
##def update(m,n,b):
##    result = account.update_many(
##    #for m in result:
##           {m: n},
##           {"$set": {m: b}}
##    )
##    print(result)
##    
##a = input("Key can sua: ")    
##n = input("gia tri cu: ")
##b = input("Gia tri can sua: ")
##update(a,n,b)
######## delete one
def delete(m,n):
    result = account.delete_many({m :n})
    print(result)
a = input("Key can xoa: ")
b= input("Gia tri can xoa: ")
delete(a,b)
