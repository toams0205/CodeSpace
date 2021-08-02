#-*- coding: utf-8 -*-
import os
import sys
import urllib.request as ul
import json

client_id = "hrDZqfChzKWif5oJw1IL"
client_secret = "eNECdOU7mK"
url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2021-05-03\",\"endDate\":\"2021-05-30\",\"timeUnit\":\"week\",\"keywordGroups\":[{\"groupName\":\"코로나\",\"keywords\":[\"코로나\",\"covid-19\",\"covid\"]} ]}"

request = ul.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = ul.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
    result_ratio = result.split('[{')
    print(result_ratio)
else:
    print("Error Code:" + rescode)