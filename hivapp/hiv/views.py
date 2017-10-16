from django.shortcuts import render
from django.http import HttpResponse
from hiv.tools import logger
from hiv.tools.loginapi import getUserInfo
from hiv.tools.verification import Verify_Rd3
from hiv.tools.exception import Unauthorized
from hiv.models import OrderInfo
from hiv.tools import mapfunc
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'home.html')

@csrf_exempt
def login(request):
    # if request.method == "POST":
    #     code = request.POST.get('code', 'code_error')
    code = getUserInfo.GetCode(request)
    session_key, openid = getUserInfo.GetSessionKey(code)
    user_info_dict = getUserInfo.UserInfomation(request, session_key)
    token = getUserInfo.Generate3rd(session_key, user_info_dict)
    token = {'code': code}
    return JsonResponse(token)


def choice(request):

    return render(request, 'choice.html')

def chat_room(request):
    return render(request, 'chat_room.html')

def me(request):
    return render(request, 'me.html')

def GenerateTime(request):
    mapfunc.place_time()
    return render(request, 'me.html')

def GenetePlace(request):
    mapfunc.place_lonlat()
    return render(request, 'me.html')

# 生成订单
def GenerateOrder(request):
    if request.method == "POST":
        createtime = request.POST.get('createtime')
        finishtime = request.POST.get('finishtime')
        place = request.POST.get('place')
        methods = request.POST.get('methods')
        rd3 = request.POST.get('rd3')
        # 先检测jwt是否是有效请求
        effection = Verify_Rd3(rd3)
        if effection:
            OrderInfo.objects.create(createtime, finishtime, place, rd3, methods)
        if not effection:
            raise Unauthorized('reregister')
        loggers = logger.LogIntoConsole()
        loggers.info('订单生成成功！')
    return True, HttpResponse(200)

