from django.shortcuts import render
from django.http import HttpResponse
from django.urls.base import reverse
from .. import models


# Create your views here.
def index(request):
    # data = models.Types.objects.extra(select = {'paths':'concat(path,id)'}).order_by ( 'paths' )

    # #if x.pid != 0:
    data = models.Types.objects.all()
    context = {'data': data}
    return render(request, "myadmin/types/index.html", context)


def add_index(request):
    return render(request, "myadmin/types/add.html")


def insert(request):
    data = request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    try:
        obj = models.Types(**data)
        obj.save()
        url = reverse("myadmin_type_index")
        status = "成功"
    except:
        url = reverse("myadmin_type_add")
        status = "失败"
    re = HttpResponse()
    re.write(f"<script>alert('{status}');location.href='{url}';</script>")
    return re


def types_del(request):
    id = request.GET.get('id')
    lev = 0
    # 获取当前id对象
    obj = models.Types.objects.get(id=id)
    if obj.fid == 0:
        lev = 1
        # 上属顶级分类
        # 获取此一级分类的子类数
        fnum = models.Types.objects.filter(fid=id).count()
        print(fnum)
    # 此为二级分类
    else:
        count = 0
        lev = 2
        data = models.Types.objects.all()
        for x in data:
            if x.sid == obj.fid:
                count += 1
        print(count)
    return HttpResponse("后台分类管理")


# 更新类别
def edit(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    id = data["id"]
    models.Types.objects.filter(id=id).update(**data)
    re = HttpResponse()
    url = reverse('myadmin_type_index')
    re.write("<script> alert('更新成功!');</script>")
    re.write("<script>location.href='" + url + "';</script>")
    return re
