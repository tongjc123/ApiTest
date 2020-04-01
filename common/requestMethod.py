#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : requestMethod.py
# Author: TongJC
# Date  : 2020-03-30

import requests

class RunMethod():

    def __init__(self):
        self.requests = requests.session()

    def post_main(self,url,header = None,data = None):
        if header !=None:
            res = self.requests.post(url =url,headers =header, data =data)
        else:
            res = self.requests.post(url=url, data =data)
        return res

    def get_main(self, url, header=None, data = None):
        if header ==None:
            res = self.requests.get(url=url, data=data)
        else:
            res = self.requests.get(url=url, headers=header, data=data)
        return res

    def postjson_main(self,url,data=None):
        res = self.requests.post(url=url, json=data)
        return res

    def delete_main(self,url,data = None):
        res = self.requests.delete(url = url,json = data)
        return res

    def run_main(self, method, url, data=None):
        if method =='postjson':
            res = self.postjson_main(url,data)
        elif method == 'post':
            res = self.post_main(url,data)
        elif method =='delete':
            res = self.delete_main(url,data)
        else:
            res = self.get_main(url,data)
        return res

myRequest = RunMethod()