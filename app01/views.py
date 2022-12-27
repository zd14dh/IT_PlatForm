from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app01 import models
import requests
import json
import datetime
# Create your views here.
from utils.MyModuleForm import ItModelForm, ApiModelForm
from utils import RequestHandler


def index(request):
    """项目主页"""
    if request.method == 'POST':
        return JsonResponse({'code': 0, 'message': '项目主页的post请求非法'})
    else:
        it_obj = models.It.objects.all()
        print('项目名称：', it_obj)
        return render(request, 'index.html', {"it_obj": it_obj})


def add_it(request):
    """添加项目"""

    if request.method == "POST":
        form_data = ItModelForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('/index/')
        else:
            return render(request, 'add_it.html', {'it_form_obj': form_data})

    else:
        it_form_obj = ItModelForm()
        return render(request, 'add_it.html', {"it_form_obj": it_form_obj})


def edit_it(request, pk):
    """编辑项目"""
    model_obj = models.It.objects.filter(pk=pk).first()
    # print(model_obj)
    if request.method == "POST":
        form_data = ItModelForm(request.POST, instance=model_obj)
        if form_data.is_valid():
            form_data.save()
            return redirect('/index/')
        else:
            return render(request, 'add_it.html', {'it_form_obj': form_data})

    else:
        it_form_obj = ItModelForm(instance=model_obj)
        return render(request, 'edit.html', {"it_form_obj": it_form_obj})


def delete_it(request, pk):
    """删除项目记录，pk项目的pk"""
    models.It.objects.filter(pk=pk).delete()
    return redirect('/index/')


def add_case_it(request, pk):
    """添加项目测试用例，pk项目的用例"""
    if request.method == 'POST':
        return JsonResponse({'code': 0, 'message': '项目主页的post请求非法'})
    else:
        it_obj = models.It.objects.all()
        return render(request, 'add_api.html', {"it_obj": it_obj})

def api_list(request,pk):
    """用例列表
        项目的pk下的用例列表
    """
    # if request.method == 'post':
    #     return JsonResponse({'code':0,'message':'项目主页的post请求非法'})
    # else:
    api_obj=models.Api.objects.filter(api_sub_it_id = pk)
    it_obj=models.It.objects.filter(pk=pk).first()
    # print(2222,api_obj,11111,it_obj)
    return render(request,'api_list.html',{'api_obj':api_obj,'it_obj':it_obj})


def add_api(request, pk):
    """添加用例,pk所属项目的pk"""

    if request.method == "POST":
        form_data = ApiModelForm(request.POST)
        if form_data.is_valid():
            print(form_data.instance.__dict__)
            form_data.instance.__dict__['api_sub_it_id'] = pk
            # form_data.instance.api_sub_it = it_obj
            form_data.save()
            return redirect('/index/')
        else:
            return render(request, 'add_api.html', {'api_form_obj': form_data})
    else:

        api_form_obj = ApiModelForm()
        it_obj = models.It.objects.filter(pk=pk).first()

        return render(request, 'add_api.html', {"api_form_obj": api_form_obj, "it_obj": it_obj})

def edit_api(request, pk):
    """编辑用例,pk所属项目的pk"""
    api_obj = models.Api.objects.filter(pk=pk).first()

    if request.method == "POST":
        form_data = ApiModelForm(request.POST,instance=api_obj)
        if form_data.is_valid():
            print(form_data.instance.__dict__)
            form_data.instance.__dict__['api_run_status']=0
            form_data.instance.__dict__['api_pass_status']=0
            form_data.instance.__dict__['api_report']=''
            form_data.save()
            return redirect(f'/api_list/{api_obj.api_sub_it_id}')
        else:
            return render(request, 'api_list.html', {'api_form_obj': form_data})
    else:
        api_form_obj = ApiModelForm(instance=api_obj)
        it_obj=models.It.objects.filter(pk=api_obj.api_sub_it_id)
        return render(request, 'edit_api.html', {"api_form_obj": api_form_obj, "it_obj": it_obj})


def delete_api(request,pk):
    '''删除用例,pk是用例pk'''
    api_obj=models.Api.objects.filter(pk=pk).first()
    api_it_id=api_obj.api_sub_it_id
    api_obj.delete()
    return redirect(f'/api_list/{api_it_id}')
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_run(request,pk=0):
    '''执行用例'''
    #如何判断请求时ajax类型
    # if request.method == "POST":
    if request.is_ajax():
        chk_value =request.POST.get('chk_value')
        chk_value =json.loads(chk_value)
        #数据库取pK在chk——value中记录对象
        api_list=models.Api.objects.filter(pk__in=chk_value)
        RequestHandler.run_case(api_list)
        return JsonResponse({"path":"logs_list"})
    else:
        case_obj=models.Api.objects.filter(pk=pk).first()
        RequestHandler.run_case([case_obj])
        # api_it_id = case_obj.api_sub_it_id
        # return redirect(f'/api_run/{api_obj.api_sub_it_id}',api_req=req.json())
        return redirect('/logs_list')

from django.http import FileResponse
from django.utils.encoding import escape_uri_path
def download_case_report(request,pk):
    '''下载测试报告'''
    case_obj = models.Api.objects.filter(pk=pk).first()
    #下载
    # case_obj.api_report=
    #下载的模板
    # file=open('crm/models.py','rb')
    response=FileResponse(case_obj.api_report)
    response['Content-Type']= 'application/octet-stream'
    response['Content-Disposition']= 'attachment;filename={}.{}'.format(escape_uri_path(case_obj.api_name),'html')
    return response


def logs_list(request):
    """log日志主页"""
    if request.method == 'POST':
        return HttpResponse("ok")
    else:
        logs_data= models.Logs.objects.all()
        return render(request,'logs_list.html', {"logs_data":logs_data})

def xrm_list(request):
    '''西人马项目列表'''
    return render(request, 'xrm_list.html')

def report_order(request,pk):
    '''查看报告预览页'''
    if request.method == 'POST':
        report_pk =request.POST.get('report_pk')
        report_obj = models.Logs.objects.filter(pk=report_pk).first()
        response = FileResponse(report_obj.log_report)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename={}.{}'.format(
            escape_uri_path(report_obj.log_sub_it.it_name), 'html')
        return response
    logs_data = models.Logs.objects.filter(pk=pk).first()
    return render(request, 'report_order.html', {"logs_data": logs_data})


def show_tab(request):
    '''可视化'''
    test_case=models.Logs.objects.first()
    
    if request.is_ajax():
        data_dict ={
            'pie':{
                'title':['通过','失败'],
                'data':[
                    {"value":test_case.log_pass_count,"name":'通过'},
                    {"value":test_case.log_failed_count,"name":'失败'},
                ]
            },
            'pie2':{
                'title':['执行','未执行'],
                'data':[
                    {"value":test_case.log_run_count,"name":"执行"},
                    {"value": test_case.log_errors_count, "name": "未执行"},

                ]
            },
            'pie3': {
                'title': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
                'data': [
                    {"value": test_case.log_run_count, "name": "执行"},
                    {"value": test_case.log_errors_count, "name": "未执行"},

                ]
            },
        }
        return JsonResponse(data_dict)
    return render(request,'show_tab.html')

def api_ajax(request):
    if request.method == 'GET':
        return JsonResponse({'code': 0, 'message': '项目主页的post请求非法'})
