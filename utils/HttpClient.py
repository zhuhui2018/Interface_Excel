#encoding:utf-8

import requests
import json

class HttpClient(object):
    def __init__(self):
        pass

    @classmethod
    def request(cls,requestUrl,requestMethod,paramsType,requestData=None,headers=None):
        if requestMethod == "post":
            if paramsType == "form":
                response = requests.post(url=requestUrl,data=json.dumps(requestData),headers=headers)
                return response
            elif paramsType == "json":
                response = requests.post(url=requestUrl, json=json.dumps(requestData))
                return response
        elif requestMethod == "get":
            if paramsType == "url":
                requestUrl == "%s%s" % (requestUrl,requestData)
                response = requests.get(url=requestUrl,headers=headers)
                return response
            elif paramsType == "params":
                if isinstance(requestData,dict):
                    response = requests.get(url=requestUrl, params=json.dumps(requestData),headers=headers)
                else:
                    response = requests.get(url=requestUrl, params=requestData, headers=headers)
                return response

if __name__ == "__main__":
    requestUrl = "http://39.106.41.11:8080/register/"
    requestMethod = "post"
    paramsType = "form"
    requestData = {"username":"sr3xasd35","password":"w29wwewac1","email":"wcx@qq.com"}
    response = HttpClient.request(requestUrl,requestMethod,paramsType,requestData)
    print(response.json())