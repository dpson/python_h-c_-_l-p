import urllib3
import certifi

import re
### C2 dung request, beautifulsoup get status( dang mắc chỗ lấy new feed lần lượt rồi cho vào list

# quanan = requests.get("https://www.facebook.com/quananngonhanoivn/?fref=ts")
#  facebook_quanan = BeautifulSoup(quanan.content ,"html.parser")
# new_feed = facebook_quanan.find("div",class_="_1dwg")
# new_feed_cont = new_feed.find("div",attrs= {"class": "_5pbx userContent"})
# print(new_feed_cont.get_text())

# chuoi_can_tim = re.compile('Món Ngon Mỗi Ngày')
# tra_ve = [x
#           for x in a
#           if re.search(chuoi_can_tim, x)]
# print(tra_ve)
def build_post_url ():
    username="quananngonhanoivn"
    graph_facebook = "https://graph.facebook.com/"
    link_end = "/posts/?key=value&access_token="
    app_id = "1592298727726686"
    app_secret = "93c85459b4a55a1c9316bfe0aebc97c5"
    post_url = graph_facebook+ username+ link_end + app_id + "|" + app_secret
    print(post_url)
    return post_url






if __name__ == "__main__":
     build_post_url()
