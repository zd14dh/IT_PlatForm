"""IT_PlatForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from app01 import views
from django.shortcuts import render,HttpResponse

def qowie(request):
    return HttpResponse("ajlkjhqelkjw")

urlpatterns = [
    #西人马列表
    path("xrm_list/",views.xrm_list,name='xrm_list'),

    path('admin/', admin.site.urls),
    path("index/",views.index,name='index'),
    #项目相关的
    path("add_it/",views.add_it,name='add_it'),
    re_path("edit_it/(?P<pk>\d+)$",views.edit_it,name='edit_it'),
    re_path("delete_it/(?P<pk>\d+)$",views.delete_it,name='delete_it'),
    #接口用例相关
    re_path("add_api/(?P<pk>\d+)$",views.add_api,name='add_api'),
    re_path("api_list/(?P<pk>\d+)$",views.api_list,name='api_list'),
    re_path("edit_api/(?P<pk>\d+)$",views.edit_api,name='edit_api'),
    re_path("delete_api/(?P<pk>\d+)$",views.delete_api,name='delete_api'),
    #用例执行
    re_path("api_run/(?P<pk>\d+)$",views.api_run,name='api_run'),
    #报告下载
    re_path("download_case_report/(?P<pk>\d+)$",views.download_case_report,name='download_case_report'),

    #log日志
    re_path("logs_list/",views.logs_list,name='logs_list'),
    re_path("report_order/(?P<pk>\d+)$",views.report_order,name='report_order'),
    re_path("show_tab/",views.show_tab,name='show_tab'),
    re_path("api_ajax/", views.api_ajax, name='api_ajax'),

]

