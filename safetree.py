#_*_ coding:utf-8 _*_
import json
from requests.auth import HTTPBasicAuth
import requests

'''创建学生帐号操作类：studentOperation'''
class studentOperation():
    '''基本学生操作'''

    def __init__(self,userName,password,newpwd=None,
                 trueName=None, grade=None,classRoom=None,className=None,
                 userAnswersValues=None,specialIdValues=None,steps=None):
        '''初始化属性userName和id'''
        self.userName = userName
        self.password = password
        self.newpwd = newpwd
        self.trueName = trueName
        self.grade = grade
        self.classRoom = classRoom
        self.className = className
        self.userAnswersValues = userAnswersValues
        self.specialIdValues = specialIdValues
        self.steps = steps
        self.s = requests.Session()    #创建Session对象实例
        self.auth = HTTPBasicAuth(userName,password)    #创建身份认证对象实例

    def Login(self):
        '''登录学生帐号'''
        url0 = 'https://guangxilogin.xueanquan.com/LoginHandler.ashx'
        values0 = {
            'jsoncallback':'jQuery16109496045507050771_1543734936625',
            'userName':self.userName,
            'password':self.password,
            'checkcode':'',
            'type':'login',
            'loginType':'1',
            'r':'0.6628292664809347',
            '_':'1543734960284'
        }
        header0 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
            'Referer': 'https://wuzhou.xueanquan.com/login.html'
        }
        response0 = self.s.get(url0,params=values0,headers=header0,timeout=5)   #传递URL参数
        #print('URL',response0.url)
        print('返回登录状态码：',response0.status_code)
        print('响应登录str内容：\n',response0.text)
        #print('cookies',response0.cookies.items())

    def specialSteps(self,step):
        '''专题教育作业模块签到'''
        url1 = 'https://huodong.xueanquan.com/p/guangxi/Topic/topic/platformapi/api/v1/records/sign'
        values1 = {"specialId":self.specialIdValues,"step":step}
        header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
        response1 = self.s.post(url1,json=values1,headers=header1,timeout=5)
        print('返回模块'+str(step)+'签到状态码：',response1.status_code)
        print('响应模块'+str(step)+'签到str内容：\n',response1.text)

    """ 模块2的作题步骤是可以跳过而直接请求签到完成的，因此此处注释掉specialStep2方法的代码
    def specialStep2(self):
        '''专题教育作业模块2'''

        userValues = {"userID":0,"userName":self.userName,"trueName":self.trueName,
                      "regionalAuthority":0, "userType":"Users","prvCode":37,
                      "cityCode":370004,"countyId":370004007,"schoolId":332317798,
                      "grade":self.grade,"classRoom":self.classRoom,
                      "className":self.className, "comeFrom":20251, "isShiYanQu":True,
                      "serverSide":"https://wuzhou.xueanquan.com"
                      }
        values2 = {'user':userValues,
                   'UserAnswers':self.userAnswersValues,
                   'specialId':self.specialIdValues,
                   'step':2
                   }
        url2 = 'https://huodong.xueanquan.com/Topic/topic/main/api/v1/records/survey'
        header2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
        response2 = self.s.post(url2,json=values2,headers=header2)
        print('返回模块2状态码：',response2.status_code)
        print('响应模块2str内容：\n',response2.text)
    """
