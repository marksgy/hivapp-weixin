import jwt
import time
import logging
#from untitled.untitled import settings
SECRET_KEY = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCIE6a1NyEFe7qCDFrvWFZiAlY1ttE5596w5dLjNSaHlKGv8AXbKg/f8yKY9fKAJ5BKoeWEkPPjpn1t9QQAZYzqH9KNOFigMU8pSaRUxjI2dDvwmu8ZH6EExY+RfrPjQGmeliK18iFzFgBtf0eH3NAW3Pf71OZZz+cuNnVtE9lrYQIDAQAB"
#session_key = 1
user_info_dict = {'nickname': 'nickname', 'gender': 'gender', 'language': 'language', 'city': 'city',
                  'province': 'province','country': 'country', 'vatarUrl': 'vatarUrl', 'id': 24324}
#openid = 'sfsdfjpdosj'
payload = {
    #"iss": settings.ISS,
    "iat": int(time.time()),
    "exp": int(time.time()) + 86400 * 31,
    # "aud": settings.AUDIENCE,
    #'id': user_info_dict['id'],
    "nickname": user_info_dict['nickname'],
}
rd3 = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
print(rd3)
if rd3:
    #session_dict = {'session_key': session_key, 'openid': openid, 'rd3': rd3}
    #SessionInfo.objects.create(session_dict)
    #logging.log('请求rd3成功!')
    token = {'access_rd3': rd3, 'account_id': user_info_dict['id']}
    print(token)