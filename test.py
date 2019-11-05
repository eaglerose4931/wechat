#coding=utf8
import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

#register reply function
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # default reply
    defaultReply = 'In the dream, auto reply'
    # tuling reply
    reply = get_response(msg['Text'])

    print(msg['Text'])
    return defaultReply

#hot start
itchat.auto_login(hotReload=True)
itchat.run()
