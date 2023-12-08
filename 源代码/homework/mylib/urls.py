from django.urls import path
from .views import *

urlpatterns = [
    # 前台首页
    path('', IndexViews.index, name='mylib_index'),
    # 分类页
    path('<int:id>', IndexViews.page, name='mylib_page'),
    # 书籍页
    path('book/<int:id>', IndexViews.book, name='mylib_book'),
    # 登录页
    path('login', IndexViews.login, name='mylib_login'),
    path('do_login',IndexViews.do_login, name='mylib_do_login'),
    path('logout',IndexViews.sign_out, name='mylib_logout'),
    # 注册页
    path('signup', IndexViews.signup, name='mylib_signup'),
    path('register', IndexViews.register, name='mylib_register'),
    path('terms', IndexViews.terms, name='mylib_terms'),
    path('reg', IndexViews.reg),
    # 个人页
    path('profile', IndexViews.profile, name="mylib_profile"),
    path('profile_edit', IndexViews.profile_edit, name="mylib_profile_edit")


]
