# -*- coding:UTF-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
# 秘钥转换方法
from django.contrib.auth.hashers import make_password
# 返回json格式数据
from django.http import HttpResponse, JsonResponse
# 将model转化为dict
from django.forms.models import model_to_dict
from utils.querySetUtils import QuerySetUtils
from utils.jsonUtils import JsonUtils

from .models import Hut
from users.models import UserProfile

# Create your views here.


class HutView(View):

    def get(self, request):
        '''
        根据小屋ID获取男女主角信息（后期可能会将小屋假定为情侣屋，还有朋友屋，还有公司员工屋，等等吧）
        :param request:
        :return:
        '''
        hutid = request.GET.get('hut')
        key = request.GET.get('key')
        hut = Hut()
        # 首先根据小屋id找
        if hutid:
            hut = Hut.objects.get(id=hutid, key=key)
        else:# 其次根据用户的最高优先级找
            token = request.COOKIES['csrftoken']
            user = UserProfile.objects.get(token=token)
            if user:
                hut = Hut.objects.get()
            else:# 如果找不到用户则返回失败
                return JsonResponse({'success': False})
        nan = UserProfile.objects.get(id=hut.nanzj)
        nv = UserProfile.objects.get(id=hut.nvzj)
        nanzj = {'user': nan.id, 'name': nan.nick_name, 'avatar': str(nan.image)}
        nvzj = {'user': nv.id, 'name': nv.nick_name, 'avatar': str(nv.image)}
        return JsonResponse({'success': True, 'nanzj': nanzj, 'nvzj': nvzj})

    def post(self, request):
        '''
        假定为：删除或者更新另一半人员（可能更偏向于删除小屋），想更新人员的话，没什么必要
        因为评价是另一个人给的，换了另一个人就全部都是重新开始，所以针对当前想法是删除小屋
        :param request:
        :return:
        '''
        pass


class HutViewList(View):

    def get(self, request):
        '''
        获取个人所有小屋--后期添加个人查询
        :param request:
        :return:
        '''
        hutList = Hut.objects.all()
        huts = QuerySetUtils.ToList(hutList)
        return JsonResponse({'success': True, 'hutList': huts})