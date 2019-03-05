# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/11/14 21:26'
import json
# 返回json格式数据
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
# 分页工具
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

from .models import TodaysMust

# 将model转化为dict
from django.forms.models import model_to_dict
from utils.querySetUtils import QuerySetUtils
from utils.jsonUtils import JsonDateUtils,JsonToBeanUtils


class TodaysMustView(View):
    def get(self, request):
        """
        获取List
        :return:
        """
        query = request.GET
        # JsonToBeanUtils.jsonToBean(get, queryTm)
        if query['zj']:
            tms = TodaysMust.objects.filter(zj=query['zj'])
            # 将数据按照10页分割
            paginator = Paginator(tms, 10)
            tms = paginator.page(query['page']).object_list
            # 将查询到的数据转化为字典
            attr = QuerySetUtils.ToList(tms)
            # 将字典中的日期字段转化为str，否则json无法格式化.
            attr = JsonDateUtils.fmtDate(attr)
            return JsonResponse({'success': True, 'todaysmust': attr})
        return JsonResponse({'success': False, 'todaysmust': []})

    def post(self, request):
        """
        保存或者更新
        :return:
        """
        obj = json.loads(request.body)
        tm = TodaysMust()
        JsonToBeanUtils.jsonToBean(obj, tm)
        tm.save()
        return JsonResponse({'success': True})