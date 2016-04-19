import urllib3
import certifi
import re
import json
import time
ten_nha_hang_s = ['quananngonhanoivn','quananngon','NhaHangAnNgon']
key_words = ["game", "sự kiện", "trúng thưởng", "quay số", "combo", "tiết kiệm", "lì xì", "event", "tặng", "miễn phí",
             "Mua 1 tặng", "GIẢM GIÁ",
             "KHUYẾN MÃI", "KHUYẾN MẠI", "SHARE", "TAG", "EVENT"]

list_post = []
i = 0
def build_post():
    for i in range(0,len(ten_nha_hang_s)-1):
        username = ten_nha_hang_s[i]
        graph_facebook = "https://graph.facebook.com"
        link_end = "posts/?key=value&access_token="
        app_id = "1253853251309235"
        app_secret = "00ce6a7c914122fdab4ab52fec44ee8d"
        post_url = graph_facebook + username + link_end + app_id + "|" + app_secret
        list_post.append(post_url)
    return(list_post)

def lay_data(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request("GET",url)
    return r.data
status_loc =[]
j = 0
for j in range(0,len(list_post)-1):
    content = lay_data(list_post[j])
    decoded_content = content.decode("utf-8")
    json_postdata = json.loads(decoded_content)
    json_status_time_vs_data = json_postdata['data']
    for per_status in json_status_time_vs_data:
        time = per_status['time']
        if time in ['time']:


########33 giả sử đã có list các newfeed cua cac page roi
### Xet post





