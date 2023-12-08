from django.urls import path
from .views import *

urlpatterns = [
    # 后台首页
    path('', IndexViews.index, name='myadmin_index'),
    # 帮助页
    path('help', IndexViews.help, name='myadmin_help'),
    # 后台登录
    path('login', IndexViews.login, name='myadmin_login'),
    path('do_login', IndexViews.do_login, name='myadmin_do_login'),
    path('verificode', IndexViews.verificode, name='myadmin_verificode'),
    path('sign_out', IndexViews.sign_out, name='myadmin_sign_out'),
    path('google_login', IndexViews.google_login, name='myadmin_google_login'),
    # 商品管理
    path('merchandise/index', MerchandiseViews.index, name='myadmin_merchandise_index'),
    path('merchandise/add', MerchandiseViews.add_index, name='myadmin_merchandise_add'),  # 添加页
    path('merchandise/insert', MerchandiseViews.add, name='myadmin_merchandise_insert'),  # 添加操作
    path('merchandise/del', MerchandiseViews.delete, name='myadmin_merchandise_delete'),  # 删除操作
    path('merchandise/edit', MerchandiseViews.edit, name='myadmin_merchandise_edit'),  # 修改页
    path('merchandise/update', MerchandiseViews.updatebook, name='myadmin_merchandise_update'),  # 修改操作
    # 用户管理
    path('users/index', UserViews.index, name='myadmin_users_index'),
    path('users/add', UserViews.add_index, name='myadmin_users_add'),  # 添加页
    path('users/insert', UserViews.insert, name='myadmin_users_insert'),
    path('users/del', UserViews.users_del, name='myadmin_users_del'),
    path('users/edit', UserViews.users_edit, name='myadmin_users_edit'),  # 修改页
    path('users/do_edit', UserViews.edit, name='myadmin_users_do_edit'),  # 修改操作
    # 分类管理
    path('type/index', TypeViews.index, name='myadmin_type_index'),
    path('type/add', TypeViews.add_index, name='myadmin_type_add'),
    path('type/edit', TypeViews.edit, name='myadmin_type_edit'),
    path('type/insert', TypeViews.insert, name='myadmin_type_insert'),
    path('type/del', TypeViews.types_del, name='myadmin_type_del'),

]
