from django.contrib import admin
from django.urls import path,include
from .import views


app_name = 'todolist'
urlpatterns = [
    path('home/', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('edit/<每一件事_id>', views.edit, name='编辑'), #前端格式  每一件事.id
    path('del/<每一件事_id>', views.delete, name='删除'), #后端格式  每一件事_id
    path('cross/<每一件事_id>', views.cross, name='划掉'), #括号里面一定不能有空格  < 每一件事_id >
]