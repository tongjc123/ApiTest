#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LWJ_case.py
# Author: TongJC
# Date  : 2020/1/8
import requests
from case.mybase import MyBase
import json,re
from common.getparam import opexcel
from common.log import atp_log

class LWJ_Case(MyBase):
    u"""LWJ登录成功"""
    def test_login_success(cls):
        atp_log.info("测试LWJ登录成功场景")
        url= 'http://cloud.sales-staging.liweijia.com/security/lv_check?type=normal&returnUrl=http%3A%2F%2Fcloud.sales-staging.liweijia.com%2F'
        atp_log.info("加载初始URL【%s】"%url)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        data = {
            "lv_username": "admin@liweijia.com",
            "lv_password": "!QAZ1qaz"
        }
        res = cls.s.post(url= url, headers = header, data= data, verify = False, allow_redirects = False)
        print(res.headers)
        #字符串操作
        #cookie_sid = res.headers['Set-Cookie'].split(';')[0]
        #cookie_LWJ = res.headers['Set-Cookie'].split(' ')[1].split(';')[0]
        #正则表达式

        cookie_sid = re.findall(r'(sid=.+api)', str(res.headers))[0]
        #print(cookie_sid)
        cookie_LWJ = re.findall(r'(LX-WXSRF-JTOKEN=.+;P)', str(res.headers))[0].split(';')[0]
        print(cookie_LWJ)

        #print(res.headers['Set-Cookie'])
        #print(cookie_LWJ)
        atp_log.info("禁止重定向，获取response headers【%s,%s】"%(cookie_sid,cookie_LWJ))
        new_cookie = cookie_sid + ';' + cookie_LWJ
        atp_log.info("组装新的headers【%s】"%new_cookie)
        url2 = 'http://cloud.sales-staging.liweijia.com/services/ums/isLogin'
        atp_log.info("加载登录验证URL【%s】"%url2)
        header2 = {
            "Cookie": new_cookie
        }
        res2 = cls.s.get(url = url2, headers = header2, verify = False)
        #print(json.loads(res2.text))
        #print(type(json.loads(res2.text)))
        hope_data = json.loads(res2.text)['result']['name']
        atp_log.info("获取验证关键信息【%s】"%hope_data)
        #print(hope_data)
        cls.assertIn("管理员",hope_data)
        atp_log.info("断言结果【%s】? =【管理员】"%hope_data)


if __name__ == '__main__':
    lwj = LWJ_Case()
    lwj.test_login_success()
