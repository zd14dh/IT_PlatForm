


'''
处理请求相关，生成测试报告
'''

import os
import json
import datetime
import requests
import unittest
from io import BytesIO
from io import StringIO
from app01 import models
from deepdiff import DeepDiff
from IT_PlatForm.settings import BASE_DIR
from HTMLTestRunner import HTMLTestRunner

class My_Case(unittest.TestCase):
    # self.response
    # self.expect
    # self.msg

    def test_case(self):
        # self._testMethodName=self.title
        self._testMethodDoc =self.desc
        self.assertEqual(DeepDiff(self.response,self.expect).get('values_changed',None),None,msg=self.msg)
        # self.assertEqual(self.response,self.expect)

class RequestOperate(object):
    def __init__(self,case_obj,suite_list):
        self.case_obj=case_obj
        self.suite_list=suite_list

    def handler(self):
        '''关于请求的一些流程
        1.提取case_obj中的字段，使用requests请求
            1.对请求参数进行校验
            2.将请求结果提出
        2.使用unittest进行断言
        3.更新数据库字段
        4.
        '''
        #发送请求，断言，生成报告
        self.send_msg()
        #更新数据库字段
        # self.update_db_status()
    def send_msg(self):
        '''发请求'''
        response=requests.request(
            # headers={"Content-Type": "application/json"},
            method=self.case_obj.api_method,
            url=self.case_obj.api_url,
            json=self._check_params(),
            # params=self._check_params()
        )
        self.assert_msg(response)

    def assert_msg(self,response):
        '''处理断言'''
        case = My_Case(methodName='test_case')
        case.response =response.json()
        case.expect = self._check_expect()
        case.msg = '自定义错误信息:{}'.format(DeepDiff(self._check_expect(),response.json()))
        case.title=self.case_obj.api_name
        case.desc=self.case_obj.api_desc

        self.suite_list.addTest(case)
        suite =unittest.TestSuite()
        suite.addTest(case)
        self.create_single_report(suite)

    def create_single_report(self,suite):
        '''生成单个用例报告
        suite:用例集
        '''
        # f = open(os.path.join(BASE_DIR,'a.html'),'wb')
        f = BytesIO()
        result=HTMLTestRunner(
            stream= f,
            # verbosity=2,
            title=self.case_obj.api_name,
            description= self.case_obj.api_desc,
        ).run(suite)

        self.update_api_status(result,f)

    def create_m_report(self,suite):
        '''生成多个用例报告
        suite:用例集
        '''
        f = BytesIO()
        result=HTMLTestRunner(
            stream = f,
            verbosity = 2,
            title=self.case_obj.api_name,
            description= self.case_obj.api_desc,
        ).run(suite)
        self.update_log_status(result,f)

    def update_log_status(self,result,f):
        '''更新log表'''
        # log_data = {'pass': 0, 'errors': 0, 'failed': 0, 'total': 0}
        # for i in result.__dict__['result']:
        #     # print(222222222222,i[0])
        #     if i[0]:
        #         log_data['failed'] += 1
        #     else:
        #         log_data['pass'] += 1
        #     log_data['total'] += 1
        # log_data['errors'] = result.__dict__['errors'].__len__()
        # 写log表，通过多少，失败多少，共执行了多少用例
        models.Logs.objects.create(
            log_report=f.getvalue().decode(encoding='utf-8'),
            log_sub_it_id=self.case_obj.api_sub_it_id,
            log_pass_count=result.__dict__['success_count'],
            log_failed_count=result.__dict__['error_count'],
            log_errors_count=result.__dict__['failure_count'],
            log_run_count=result.__dict__['testsRun'],
        )

    def update_api_status(self,result,f):
        '''更新数据库字段
            1.api_report
            2.api_pass_status
            3.api_run_status
            4.api_run_time
        '''
        #写报告
        obj= models.Api.objects.filter(pk=self.case_obj.pk).first()
        obj.api_report= f.getvalue().decode(encoding='utf-8')
        #写执行之间
        obj.api_run_time= datetime.datetime.now()
        #写是否执行
        obj.api_run_status=1
        # 写是否通过
        for i in result.__dict__['result']:
            if i[0] :
                obj.api_pass_status=0
            else:
                obj.api_pass_status=1
        obj.save()


    def _check_expect(self):
        """校验请求的expect参数
                默认，数据库中的expect字段是标准的json串
        """
        if self.case_obj.api_exprct:
            return json.loads(self.case_obj.api_exprct)
        else:
            return {}

    def _check_data(self):
        """校验请求的data参数
                默认，数据库中的data字段是标准的json串
        """
        if self.case_obj.api_data:
            return json.loads(self.case_obj.api_data)
        else:
            return {}

    def _check_params(self):
        '''校验请求的data参数'''
        if self.case_obj.api_params:
            return json.loads(self.case_obj.api_params)
        else:
            return {}

def run_case(api_list):
    # print(api_list)
    suite_list=unittest.TestSuite()
    for i in api_list:
        RequestOperate(case_obj=i,suite_list=suite_list).handler()

    # print(11111,suite_list)
    RequestOperate(case_obj=i,suite_list=suite_list).create_m_report(suite_list)
