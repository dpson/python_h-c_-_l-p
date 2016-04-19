import re
mesage = "toi hoc lop mot. Ban Son cao . Toi hoc cao hoc. Bạn Nam cao"
keyword = 'toi hoc'
status = re.search(keyword, mesage)
print(status)
print(status.groups())
