from bs4 import BeautifulSoup
import requests
quan_an_dem = requests.get("https://www.facebook.com/quanandemhn/?fref=ts")
quan_an_dem_html = BeautifulSoup(quan_an_dem.content,"html.parser")
new_feed = quan_an_dem_html.find("div",class_="_1dwg")
liketong = new_feed.find("div",class_="_4arz")
print(liketong)
# comments = commenttong.find_all("div",attrs={"class" : "UFIRow UFIComment _4oep", "role" : "article","aria-label":"Bình luận" })
# print(len(comments))
