import jwt
import time
from random import randint
from django.views.decorators.csrf import csrf_exempt
from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
from weixin.oauth2 import OAuth2AuthExchangeError
from hivapp import settings
from hiv.models import SessionInfo, UserInfo
from hiv.tools.exception import Unauthorized, ServerError
from hiv.tools import logger


@csrf_exempt
class getUserInfo(object):


    # 获取从客户端请求的code
    @csrf_exempt
    def GetCode(request):
        if request.method == "POST":
            code = request.POST.get('code', 'code_error')
            return code

    # 使用code换取session_key
    def GetSessionKey(code):
        appid = settings.WXAPP_ID
        secret = settings.WXAPP_SECRET
        api = WXAPPAPI(appid=appid, app_secret=secret)
        try:
            session_info = api.exchange_code_for_session_key(code=code)
        except OAuth2AuthExchangeError as e:
            raise Unauthorized(e.code, e.description)

        session_key = session_info.get('session_key')
        openid = session_info.get('openid')
        print(openid)
        print(session_key)
        return session_key, openid

    # 从session_info解密得到用户信息
    def UserInfomation(request, session_key):

        if request.method == "POST":
            encrypted_data = request.POST.get('encrypted_data')
            iv = request.POST.get('iv')
            signature = request.POST.get('signature')
            crypt = WXBizDataCrypt(settings.WXAPP_ID, session_key)

            user_info = crypt.decrypt(encrypted_data, iv)
            openid = user_info.get('openId')
            nickname = user_info.get('nickname')
            gender = user_info.get('gender')
            language = user_info.get('language')
            city = user_info.get('city')
            province = user_info.get('province')
            country = user_info.get('country')
            vatarUrl = user_info.get('vatarUrl')
            id = randint(1,999999999999999)
            user_info_dict = {'nickname': nickname, 'gender': gender, 'language': language, 'city': city,
                              'province': province, 'country': country, 'vatarUrl': vatarUrl, 'id': id, 'openid':openid}
            if request.method == "POST":
                approach = request.POST.get('auth_approach')
            if approach == 'wxapp':
                account = UserInfo.objects.create(user_info_dict)
                if not account:
                    return False, ServerError('register_fail')
                return user_info_dict



    # 新用户创建rd3验证码
    def Generate3rd(request, session_key, user_info_dict):

        payload = {
            "iss": settings.ISS,
            "iat": int(time.time()),
            "exp": int(time.time()) + 86400 * 31,
            "aud": settings.AUDIENCE,
            'id': user_info_dict['id'],
            "nickname": user_info_dict['nickName'],
        }
        rd3 = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        if rd3:
            session_dict = {'session_key': session_key, 'openid': user_info_dict['openid'], 'rd3': rd3}
            SessionInfo.objects.create(session_dict)
            loggers = logger.LogIntoConsole()
            loggers.info('订单生成成功！')
            token = {'access_rd3': rd3, 'account_id': user_info_dict['id']}
            return token

