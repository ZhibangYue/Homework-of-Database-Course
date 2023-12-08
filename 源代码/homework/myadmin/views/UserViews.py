import os

from django.shortcuts import render
from django.urls.base import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from mylib import models


# Create your views here.
def index(request):
    data = models.Users.objects.all()
    context = {'data': data}
    return render(request, "myadmin/users/index.html", context)


def add_index(request):
    return render(request, "myadmin/users/add.html")


def insert(request):
    # 接受数据
    data = request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    # 密码加密
    data["password"] = make_password(data["password"], None, "pbkdf2_sha256")
    # 头像检测
    file = request.FILES.get("profile", None)
    try:
        if file:
            filename = imgupload(file)
            data["profile"] = filename
        else:
            data.pop("profile")
        # 同步至数据库
        obj = models.Users(**data)
        obj.save()
        url = reverse("myadmin_users_index")
        status = "成功"
    except:
        url = reverse("myadmin_users_add")
        status = "失败"
    re = HttpResponse()
    re.write(f"<script>alert('{status}');location.href='{url}';</script>")
    return re


# 图片上传函数
def imgupload(file):
    import random, time
    # 后缀名
    print(file)
    zh = file.name.split(".").pop()
    name = str(random.randint(10000, 99999) + time.time()) + "." + zh
    with open(f'./static/uploads/{name}', "wb+") as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    filename = f"/static/uploads/{name}"
    return filename


def users_del(request):
    id = request.GET.get("id")
    obj = models.Users.objects.get(id=id)
    try:
        if "uploads" in obj.profile:
            os.remove("." + obj.profile)
    except:
        return JsonResponse({"code": 1, "msg": "图片删除失败"})
    obj.delete()
    return JsonResponse({"code": 20000, "msg": "删除成功"})


def users_edit(request):
    id = request.GET.get("id")
    obj = models.Users.objects.get(id=id)
    return render(request, 'myadmin/users/edit.html', {"obj": obj})


def edit(request):
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    file = request.FILES.get("profile", None)
    id = data["id"]
    old_data = models.Users.objects.get(id=id)
    # 接受到上传的新图片
    if file:
        old_img_url = "." + old_data.profile
        filename = imgupload(file)
        data['profile'] = filename
        # 如果是默认头像，则不删除
        if old_img_url != "./static/favicon.ico":
            os.remove(old_img_url)
    # 图片未更改
    else:
        data["profile"] = old_data.profile
    # 检测密码是否更改
    password = request.POST.get("password", None)
    if password:
        data["password"] = make_password(data["password"], None, "pbkdf2_sha256")
    else :
        data["password"] = old_data.password
    re = HttpResponse()
    try:
        models.Users.objects.filter(id=id).update(**data)
        url = reverse('myadmin_users_index')
        re.write("<script> alert('更新成功!');</script>")
    except:
        re.write("<script> alert('更新失败！');</script>")
        url = reverse('myadmin_users_edit')
    re.write("<script>location.href='" + url + "';</script>")
    return re