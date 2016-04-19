from firebase import firebase
fb = firebase.FirebaseApplication('https://hiepxanh.firebaseio.com/user/',None)
result = fb.get('/user',None)
##for key,value in result.items():
##    print(value['name'],':',value['text'])
    
    #print(key,'===>',value)
##    for key,value in value.items():
##        print(key, ':',value)
fb = firebase.FirebaseApplication('https://techkids-c4e.firebaseio.com/',None)
result=fb.post('', ({'name': "sexy", 'title': 'share film porn', 'content': "can lam 1 duong linkk cua mariaozawoa"}))
print(result)
