# Access to tinhte.vn
import requests
tinhte = requests.get("https://tinhte.vn/")
print(tinhte)

#load tinhte.vn to BeautifulSoup
from bs4 import BeautifulSoup
trangweb_tinhte = BeautifulSoup(tinhte.content,"html.parser")

# locate big footer
bigfooter = trangweb_tinhte.find("ul",attrs={"class":"bigFooterRow bigFooterRow--mainRow bigFooterRow--has4Columns"})

# processing the target
footer_target =bigfooter.li.div.ul
import re
def menu_without_advertise (href):
     return href and  re.compile("tinhte.vn").search(href)
result = footer_target.find_all(href= re.compile("quangcao"))
for x in result:
    print(x.get_text())