# _*_ coding:utf-8 _*_
import requests
import openpyxl
import re

class adminOperate():
    '''学校管理员操作'''

    def __init__(self,userName='xiaoweilin3',password='sihe8356091'):
        '''初始化管理员帐号及密码'''
        self.userName = userName
        self.password = password
        self.s = requests.Session()

    def Login(self):
        '''管理员登录'''
        url0 = 'https://guangxilogin.xueanquan.com/LoginHandler.ashx'
        values0 = {
            'userName': self.userName,
            'password': self.password,
            'type': 'login',
            'loginType': '1'
            }
        header0 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
            'Referer	': 'https://wuzhou.xueanquan.com/login.html'
            }
        response0 = self.s.get(url0,params=values0,headers=header0)
        print('登录状态码：',response0.status_code)
        print('登录响应str内容：',response0.text)
        print()
