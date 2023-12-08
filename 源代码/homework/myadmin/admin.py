from django.contrib import admin
from .models import Books, Admin_Users


# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ('id', 'name', 'author', 'price', 'publisher', 'pub_date', 'abstract', 'pic')
    # 排序，负号表示降序
    ordering = ('id',)
    # list_edit可编辑字段=['']
    # list_per_page每页显示数量
    # search_filed搜索字段=('')
    # 过滤器list_filter=('')
    # date_hierarchy = ('')

class AdminsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'password', 'phone', 'sex', 'registerdate', 'profile')
    # 排序，负号表示降序
    ordering = ('id',)

admin.site.register(Books, BooksAdmin)
admin.site.register(Admin_Users, AdminsAdmin)
