import requests
import base64
import hashlib
import hmac
from urllib import parse
import urllib3
import time

#1.AK/SK/host、method、url绝对路径、querystring
# AK = '827cef164a084ee082ada4c01e99e29d'
# SK = '6dd2691ce7a54187b9190bda4a77212a'
# host='bcc.su.baidubce.com'
# method = 'PUT'
# query = 'modifyAtribute'
# URI='/v2/instance/i-AqYfCEgy'
#
# #2.x-bce-date
# x_bce_date=time.gmtime()
# x_bce_date=time.strftime('%Y-%m-%dT%H:%M:%SZ',x_bce_date)
# # print(x_bce_date)
#
# #3.headers和signedHeaders
# header ={
#     'content-type':'application/json;charset=utf-8',
#     'Host':host,
#     'x-bce-date':x_bce_date
# }
# signedHeaders = 'content_type;host;x-bec-date'
#
# #4.认证字符串前缀
# authStringPrefix ='bce-auth-v1'+'/'+AK+'/'+x_bce_date+'/'+'1800'
#
# #5.生成CanonicalRequest
# #5.1生成CanonicalURI
# CanonicalURI = parse.quote(URI)
#
# #5.2生成CanonicalQueryString
# CanonicalQueryString =query + '='
#
# #5.3生成CanonicalHeaders
# result = []
# for key,value in header.items():
#     tempStr = str(parse.quote(key.lower(),safe='')) +":" +str(parse.quote(value,safe=""))
#     result.append(tempStr)
# result.sort()
# CanonicalHeaders='\n'.join(result)
#
# #5.4凭借得到CanonicalRequest
# CanonicalRequest =method+'\n'+CanonicalURI+'\n'+CanonicalQueryString +'\n'+CanonicalHeaders
#
# #6.生成signingKey
# signingKey =hmac.new(SK.encode('utf-8'),authStringPrefix.encode('utf-8'),hashlib.sha256)
#
# #7.生成Signature
# Signature = hmac.new((signingKey.hexdigest()).encode('utf-8'),CanonicalRequest.encode('utf-8'),hashlib.sha256)
#
# #8.生成Authorization并放到header里
# header['Authorization']=authStringPrefix+'/'+signedHeaders+'/'+Signature.hexdigest()

#获取图像识别access_token
# API_KEY='6aHMGCgAwRZlNa0gkQerraBp'
# Secret_Key='gISvVReWp84z175lGOyIwUry4LMFxb7Q'
# host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={Secret_Key}'
# response = requests.get(host)
# if response:
#     print(response.json())


#获取文字识别access_token
# API_KEY='VLEfQrAmoR4vV9auSszGBDBG'
# Secret_Key='3D3mBrUA0Gd8PxOKBgN83FKksc7FAITQ'
# host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={Secret_Key}'
# response = requests.get(host)
# if response:
#     print(response.json())

#通用物体和场景识别
request_url = " https://aip.baidubce.com/api/v1/solution/direct/imagerecognition/combination"
#图像单主体检测
request_url1 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
#动物识别
request_url2 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
#logo识别
request_url3 = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"

#通用文字识别（高精度含位置版）
request_url4 = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
#通用文字识别（标准版）
request_url5 = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
#通用文字识别（标准含位置版）
request_url6 = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"

#识别验证码
def open_image():
    # 二进制方式打开图片文件
    request_url5 = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    f = open('image.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img,'language_type':'ENG'}
    # access_token = '24.c49720975f538cd2d48a6d42a8da224d.2592000.1668932165.282335-28019501'
    access_token = '24.e6b824cf1a595ffb5031730eb959f899.2592000.1668933090.282335-28018980'
    request_url5 = request_url5 + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url5, data=params, headers=headers)
    if response:
        print (response.json())

        return response.json()

