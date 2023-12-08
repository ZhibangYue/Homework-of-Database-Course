from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 后台首页（已登录）
from myadmin import models


def index(request):
    return render(request, 'myadmin/index.html')


# 后台登录页面
def login(request):
    return render(request, 'myadmin/login.html')


# 后台登录验证
def do_login(request):
    data = request.POST.dict()
    data.pop("csrfmiddlewaretoken")

    # 检验验证码
    if request.session['verificode'] != data['verificode']:
        return HttpResponse("<script>alert('验证码错误!');history.back();</script>")
    # 检测用户名
    obj = models.Admin_Users.objects.filter(nickname=data['nickname'])

    if obj.count() == 0:
        return HttpResponse("<script>alert('用户名或密码错误！');history.back();</script>")
    # 检测密码
    from django.contrib.auth.hashers import make_password, check_password
    # 密码正确则登录
    if check_password(data['password'], obj[0].password):
        request.session['AdminUser'] = {'id': obj[0].id, 'nickname': obj[0].nickname, 'phone': obj[0].phone,
                                        'profile': obj[0].profile}
        from django.urls.base import reverse
        url = reverse("myadmin_index")
        return HttpResponse(f"<script>alert('登录成功！');location.href='{url}';</script>")
    # 若密码不正确
    else:
        return HttpResponse("<script>alert('用户名或密码错误！');history.back();</script>")


# 谷歌登录
def google_login(request):
    return HttpResponse(
        "<script>alert('由于Google拒绝遵守中国的法律，因此我们不在内地采用引入谷歌认证的登录方式。');history.back();</script>")


# 验证码
def verificode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 30
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = '123456789ABCDEFGHIJKLMNPQRSTUVWXYZ'
    # 选取字符组成验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randint(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('msyh.ttc', 25)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制四个字符
    draw.text((3, 1), rand_str[0], font=font, fill=fontcolor)
    draw.text((30, 1), rand_str[1], font=font, fill=fontcolor)
    draw.text((57, 1), rand_str[2], font=font, fill=fontcolor)
    draw.text((84, 1), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session,用于进一步验证
    request.session["verificode"] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中
    im.save(buf, 'png')
    # 将内存中的图片数据返回客户端，媒体类型（MIME）为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


# 退出登录
def sign_out(request):
    request.session.flush()
    from django.urls.base import reverse
    url = reverse("myadmin_login")
    return HttpResponse(f"<script>alert('退出登录成功！');location.href='{url}';</script>")


# 帮助页
def help(request):
    return HttpResponse("帮助")
