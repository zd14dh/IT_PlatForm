import requests
import time
import json
from app01.baiduyun import open_image

class API_TEST():
    def __init__(self):
        name= 'admin@shagang.com'
        pwd = 'shagang2021!@#'
        ip= '172.28.2.185'
        port = '8088'
        token = "空"
        self.name=name
        self.pwd=pwd
        self.url='http://'+ip+':'+ port
        self.jsonheader= {'Content-Type': 'application/json','charset':'UTF-8'}
        self.imageheader= {'Content-Type': 'image/jpeg','charset':'UTF-8'}
        self.token =token

    #图片请求
    def image_name(self):
        req=requests.get(url='http://172.28.2.185:8088/api/v1/cms/public/code/1666244578176',headers=self.imageheader)
        req.raise_for_status()
        req.encoding =req.apparent_encoding
        with open('image.png','wb')as f:
            for data in req.iter_content(128):
                f.write(data)

    #登录
    def api_login(self,code):
        # 用户登录
        data={"account": "admin@shagang.com", "credential": "c2hhZ2FuZzIwMjEhQCM=", "randomStr": "1666244578176","code": code}
        print(data)
        req=requests.api.post(url=self.url+'/api/v1/cms/login',json=data,headers=self.jsonheader)
        token=req.json()
        self.token=token
        return token
    #用户规则
    def user_rols(self):
        #用户权限接口
        self.jsonheader["Authorization"]=self.token
        req=requests.api.post(url=self.url+'/api/v1/cms/users/roles',headers=self.jsonheader)
        return req

    #

    def read_apijson(self):
        with open('api (2).json','r',encoding='utf-8')as f:
            api=f.read()
            json_list=json.loads(api)
            p = 0
            for list in json_list:

                for l in list['list']:
                    req_list = {
                        'title': l['title'],
                        'path': l['path'],
                        'method': l['method'],
                        'req_query_list': {}
                    }
                    for q in l["req_query"]:
                        req_list["req_query_list"]["{}".format(q["name"])]=q["desc"]
                    p=p+1
                    print(p,req_list)

if __name__ == '__main__':
    # apijson=API_TEST().read_apijson()
    # roles=rep.user_rols()
    pict=open_image()
    print(pict)