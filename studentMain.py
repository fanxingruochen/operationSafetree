#_*_ coding:utf-8 _*_
import safetree
import openpyxl

wb = openpyxl.load_workbook('studentIFMT.xlsx')
sheet = wb['Sheet0']
n = 0
m = 9 #sheet.max_row
print('最大行号：',m)
#usernames = open('UName.txt')
"""
userAnswersValues = [ #答案参数
                {"module":1,"id":1,"type":"Radio","answer":"A"},
                {"module":1,"id":2,"type":"Radio","answer":"B"},
                {"module":1,"id":3,"type":"Radio","answer":"B"},
                {"module":1,"id":4,"type":"Radio","answer":"A"},
                {"module":1,"id":5,"type":"Radio","answer":"C"},
                {"module":1,"id":6,"type":"CheckBox","answer":"F"},
                {"module":1,"id":7,"type":"Radio","answer":"E"},
                {"module":1,"id":8,"type":"Radio"},
                {"module":1,"id":9,"type":"Radio"},
                {"module":1,"id":10,"type":"CheckBox","answer":"I"},
                {"module":1,"id":11,"type":"Radio","answer":"C"},
                {"module":1,"id":12,"type":"CheckBox","answer":"F"},
                {"module":1,"id":13,"type":"Radio","answer":"A"},
                {"module":1,"id":14,"type":"Radio","answer":"A"},
                {"module":1,"id":15,"type":"Radio","answer":"C"}
                ]
"""
for i in range(3,m,1):
    userName = sheet['B'+str(i)].value
    password = 'shxx2018'
    """
    trueName = sheet['C'+str(i)].value
    grade = sheet['D'+str(i)].value
    classRoom = sheet['E'+str(i)].value
    className = sheet['F'+str(i)].value
    """
    specialIdValues = 243
    step1 = 1
    step2 = 2
    stuDoWork = safetree.studentOperation(userName,password,
                                          specialIdValues=specialIdValues)
    stuDoWork.Login()
    for step in range(step1,step2+1,1):
        """
        stuDoWork = safetree.studentOperation(userName,password,trueName=trueName,
                                              grade=grade,classRoom=classRoom,
                                              className=className,
                                              userAnswersValues=userAnswersValues,
                                              specialIdValues=specialIdValues)
        """
        stuDoWork.specialSteps(step)
        print('模块'+str(step))
    n += 1
    print('计数：',n,'\n','\n')

'''
for line in usernames:
    print('帐号：',line,end='')
    user = str(line).strip()
    stdOperate = safetree.studentOperation(user,'shxx2018')
    stdOperate.Login()
    stdOperate.specialStep1()
    stdOperate.specialStep2()
    n += 1
    print('计数：',n,'\n','\n')
'''
