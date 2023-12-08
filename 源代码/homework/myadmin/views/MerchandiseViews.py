from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .. import models
from django.urls.base import reverse


# Create your views here.
def index(request):
    data = models.Books.objects.all()
    context = {'data': data}
    return render(request, 'myadmin/merchandise/index.html', context)


def add_index(request):
    data = models.Types.objects.all()
    context = {'data':data}
    return render(request, 'myadmin/merchandise/add_index.html',context)


def add(request):
    # 接受数据
    data = request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    # 头像检测
    pic = request.FILES.get("pic", None)
    try:
        if pic:
            filename = imgupload(pic)
            data["pic"] = filename
        else:
            data.pop("pic")
        # 同步至数据库
        obj = models.Books(**data)
        obj.save()
        url = reverse("myadmin_merchandise_index")
        status = "成功"
    except:
        url = reverse("myadmin_merchandise_add")
        status = "失败"
    re = HttpResponse()
    re.write(f"<script>alert('{status}');location.href='{url}';</script>")
    return re


# 图片上传函数
def imgupload(file):
    import random, time
    # 后缀名
    zh = file.name.split(".").pop()
    name = str(random.randint(10000, 99999) + time.time()) + "." + zh
    with open(f'./static/uploads/{name}', "wb+") as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    filename = f"/static/uploads/{name}"
    return filename


# 商品删除
def delete(request):
    id = request.GET.get("id")
    obj = models.Books.objects.get(id=id)
    try:
        if "uploads" in obj.pic:
            import os
            os.remove("." + obj.pic)
    except:
        return JsonResponse({"code": 1, "msg": "图片删除失败"})
    obj.delete()
    return JsonResponse({"code": 20000, "msg": "删除成功"})


# 编辑页
def edit(request):
    id = request.GET.get("id")
    obj = models.Books.objects.get(id=id)
    return render(request, 'myadmin/merchandise/edit.html', {"obj": obj})


# 更新
def updatebook(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    file = request.FILES.get("pic", None)
    id = data["id"]
    old_data = models.Books.objects.get(id=id)
    # 接受到上传的新图片
    if file:
        old_img_url = "." + old_data.pic
        filename = imgupload(file)
        data['pic'] = filename
        import os
        os.remove(old_img_url)
    # 图片未更改
    else:
        data["pic"] = old_data.pic
    re = HttpResponse()
    try:
        models.Books.objects.filter(id=id).update(**data)
        url = reverse('myadmin_merchandise_index')
        re.write("<script> alert('更新成功!');</script>")
    except:
        re.write("<script> alert('更新失败！');</script>")
        url = reverse('myadmin_merchandise_edit')
    re.write("<script>location.href='" + url + "';</script>")
    return re
