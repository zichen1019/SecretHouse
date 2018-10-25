# -*- coding:UTF-8 -*-
import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
# 获取token
from django.middleware.csrf import get_token
# 关闭csrf验证，用于某个方法在方法上一行加@csrf_exempt
from django.views.decorators.csrf import csrf_exempt
# 将model转化为dict
from django.forms.models import model_to_dict

from .forms import LoginForm, RegisterForm
from .models import UserProfile, UserAttr
from utils.email_send import send_register_email
from utils.querySetUtils import QuerySetUtils
from utils.jsonUtils import JsonUtils

# Create your views here.


# 重写认证方法
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # get方法只能获取一个，如果有多个就会报错
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 重写view
class LoginView(View):

    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(user_name = user_name, password = pass_word)
            if user is not None:
                login(user_name, pass_word)
                return render(request, 'index.html', {})
            else:
                # 未从书库中读取到对应的信息
                return render(request, 'login.html', {'msg', '用户名或密码错误'})
        else:
            # 验证失败
            return render(request, 'login.html', {'login_form':login_form})


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        print(register_form.errors)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)

            # 发送包含注册激活链接的邮件给用户
            # send_register_email(user_name, 'register')

            user_profile.save()
        return render(request, 'register.html', {})


class PersonalAttrView(View):

    # from django.views.decorators.csrf import ensure_csrf_cookie
    def get(self,request):
        '''
        获取个人数据
        :param request:
        :return:
        '''
        attrId = request.GET.get('id', '')
        if attrId:
            # 根据id查询,特别注意 调用objects时一定要用类，而不要用对象调用objects，否则报错：无此实例对象
            userAttrs = UserAttr.objects.filter(id=attrId)
            # 将查询到的数据转化为字典
            attr = QuerySetUtils.ToList(userAttrs)
            # 将字典中的日期字段转化为str，否则json无法格式化.
            # attr[0]['add_time'] = attr[0]['add_time'].strftime("%Y-%m-%d %H:%M:%S")
            attr = JsonUtils.fmtDate(attr)
            res = {
                'success': True,
                'attribute': attr[0]
            }
            '''
            # 将对象格式化为字符串
            result = json.dumps(res, ensure_ascii=False)
            # 将字符串返回给前端,按Json格式返回
            return HttpResponse(result, content_type='application/json')
            '''
            # 使用此方式返回结果  如果数据是list列表，需要这样写return JsonResponse(res, safe=False)就可以正常返回json数据了
            return JsonResponse(res)
        return JsonResponse({'success': False, 'reason': '数据不存在！'})


    def post(self,request):
        '''
        更新数据
        :param request:
        :return:
        '''
        attr = UserAttr()
        obj = json.loads(request.body)
        attr.id = obj['id']
        attr.attrname = obj['attrname']
        attr.features = obj['features']
        attr.progress = obj['progress']
        attr.index = obj['index']
        attr.status = obj['status']
        userProfile = UserProfile()
        userProfile.id = obj['user']
        attr.user = userProfile
        attr.save()
        return JsonResponse({'success': True})


class PersonalAttrViewList(View):

    def get(self, request):
        '''
        获取个人所有信息
        :param request:
        :return:
        '''
        userId = request.GET.get('user', '')
        if userId:
            userAttrs = UserAttr.objects.filter(user_id=userId)
            attrList = QuerySetUtils.ToList(userAttrs)
            return JsonResponse({'success': True, 'attrList': attrList})
        return JsonResponse({'success': False, 'reason': '用户不存在！'})

    def post(self, request):
        return JsonResponse({'success': False, 'reason': '请求未处理！'})


class ApiLoginView(View):

    def get(self, request):
        token = request.GET.get('token', '')
        user_profile = UserProfile.objects.get(token=token)
        if user_profile:
            user = model_to_dict(user_profile)
            user['roles'] = ['editor']
            user['image'] = str(user['image'])
            return JsonResponse({'success': True, 'user': user})
        else:
            return JsonResponse({'success': False})

    def post(self, request):
        obj = json.loads(request.body)
        username = obj['username']
        password = obj['password']
        token = request.COOKIES['csrftoken']
        print('username:' + username + '    ' + 'password:' + password+'     '+'token:'+token)
        user_profile = authenticate(username=username, password=password)
        if user_profile is not None:
            user_profile.token = token
            user_profile.save()
            return JsonResponse({'success': True, 'token': token})
        else:
            return JsonResponse({'success': False})


class Tokens(View):

    def get(self, request):
        token = get_token(request)
        return JsonResponse({'success': True, 'token': token})