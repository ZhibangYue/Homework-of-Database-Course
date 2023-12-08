from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from myadmin import models
from .. import models as models_lib


# Create your views here.
# 后台首页（已登录）


def index(request):
    data = models.Books.objects.all()
    type = models.Types.objects.all()
    length = data.count()  # 获取表数据总长度
    length2 = models_lib.Users.objects.count()
    result = data[length - 5:length]
    context = {'data': data, 'type': type, 'book': list(result), 'length': length, 'length2': length2}
    return render(request, 'mylib/index.html', context)


def page(request, id):
    type = models.Types.objects.all()
    typename = type.filter(id=id).first().name
    data = models.Books.objects.filter(type=typename)
    count = data.count()
    context = {'data': data, 'type': type, 'id': int(id), 'title': list(type)[id - 1].name, 'count': count}
    return render(request, 'mylib/page.html', context)


# 书籍详情页
def book(request, id):
    type = models.Types.objects.all()
    data = models.Books.objects.filter(id=id).first()
    typename = data.type
    id2 = type.filter(name=typename).first().id
    context = {'book': data, 'type': type, 'id': id2, 'title': data.name}
    return render(request, 'mylib/book.html', context)


# 后台登录页面
def login(request):
    return render(request, 'mylib/login.html')


# 后台登录验证
def do_login(request):
    data = request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    # 检验验证码
    if request.session['verificode'] != data['verificode']:
        return HttpResponse("<script>alert('验证码错误!');history.back();</script>")
    # 检测用户名
    obj = models_lib.Users.objects.filter(phone=data['phone'])

    if obj.count() == 0:
        return HttpResponse("<script>alert('手机号未注册或密码错误！');history.back();</script>")
    # 检测密码
    from django.contrib.auth.hashers import make_password, check_password
    # 密码正确则登录
    if check_password(data['password'], obj[0].password):
        request.session['User'] = {'id': obj[0].id, 'nickname': obj[0].nickname, 'phone': obj[0].phone,
                                   'email': obj[0].email,
                                   'profile': obj[0].profile}
        from django.urls.base import reverse
        url = reverse("mylib_index")
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
    url = reverse("mylib_login")
    return HttpResponse(f"<script>alert('退出登录成功！');location.href='{url}';</script>")


# 注册
def signup(request):
    return render(request, "mylib/signup.html")


def register(request):
    # 接受数据
    data = request.POST.dict()
    re = HttpResponse()
    obj0 = models_lib.Users.objects.filter(phone=data['phone']).count()
    obj1 = models_lib.Users.objects.filter(email=data['email']).count()
    if obj0 != 0 or obj1 != 0:
        status = "手机号或电子邮箱已被注册，注册失败！"
        url = reverse("mylib_signup")
        del request.session["verify"]
    elif data["verify"] != request.session['verify']:
        status = "验证码错误，注册失败！"
        url = reverse("mylib_signup")
    else:
        data.pop("csrfmiddlewaretoken")
        data.pop("verify")
        # 密码加密
        data["password"] = make_password(data["password"], None, "pbkdf2_sha256")
        # 同步至数据库
        try:
            obj = models_lib.Users(**data)
            obj.save()
            url = reverse("mylib_login")
            status = "注册成功"
            del request.session["verify"]
        except:
            url = reverse("mylib_signup")
            status = "注册失败"

    re.write(f"<script>alert('{status}');location.href='{url}';</script>")
    return re


def sendMessage(email):  # 发送邮件并返回验证码
    # 生成验证码
    import random
    str1 = '0123456789'
    rand_str = ''
    for i in range(0, 6):
        rand_str += str1[random.randrange(0, len(str1))]
    # 发送邮件：
    # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
    message = "您的验证码是" + rand_str + "，10分钟内有效，请尽快填写"
    emailBox = []
    emailBox.append(email)
    send_mail('图书馆注册验证码', message, 'yuezhibang@mail.sdu.edu.cn', emailBox, fail_silently=False)
    return rand_str


def reg(request):
    import json
    if request.POST.get('type') == 'sendMessage':
        print(request.POST.get('email'))
        email = request.POST.get('email')
        response = {"state": False, "errmsg": ""}

        try:
            rand_str = sendMessage(email)  # 发送邮件
            request.session['verify'] = rand_str  # 验证码存入session，用于做注册验证
            response['state'] = True
        except:
            response['errmsg'] = '验证码发送失败，请检查邮箱地址'
        return HttpResponse(json.dumps(response))


def terms(request):
    return HttpResponse("<h1>略</h1><p>谁会看这玩意</p>")

# 个人页
def profile(request):
    id = request.session["User"]["id"]
    type = models.Types.objects.all()
    data = models_lib.Users.objects.filter(id=id).first()
    context = {"type": type, "data": data}
    return render(request, 'mylib/profile.html', context)


def profile_edit(request):
    id = request.session["User"]["id"]
    data = request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    re = HttpResponse()
    try:
        models_lib.Users.objects.filter(id=id).update(**data)
        status = "修改成功"
    except:
        status = "修改失败"
    url = reverse("mylib_profile")
    re.write(f"<script>alert('{status}');location.href='{url}';</script>")
    return re
