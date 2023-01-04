import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import os
import datetime
import time
import os.path
'''定义状态符号'''
IS_NOT_COUNTING=0
IS_COUNTING=1


'''基本操作'''
def app_path():
    import sys
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)            #没打包前的py目录


def mkdir(path):#创建文件夹目录
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)


def save_txt(path,txt):
    with open(path,'w') as f:
        f.write(txt)


def refine_FileName(FilePath:str):#提取文件的名字并返回合适格式的文件路径
    file_splited=FilePath.split('\\')
    FileName=file_splited[-1]
    return FileName , '/'.join(file_splited)


def load_name_list():#加载名单信息
    NameList=[]
    NameNumDic={}
    NameListPath=app_path()+'/名单.hwa'
    try:
        with open(NameListPath) as f:
            if NameList!=[]:
                NameList=[]

            for line in f:
                if line[-1]=='\n' or line[-1]=='\r':
                    line = line[:-1]
                list_=line.split('\t')
                name=None
                numb=None

                if len(list_[0])>0:
                    if len(list_)==1:
                        if '0'<=list_[0][0]<='9':
                            pass
                        else:
                            name=list_[0]
                    elif len(list_)==2:
                        if '0'<=list_[0][0]<='9':
                            name=list_[1]
                            numb=list_[0]
                        else:
                            name=list_[0]
                            numb=list_[1]
                    
                    if name in ['',' ','  ','   ','    ']:#去除空行
                        continue

                    NameList.append(name)
                    if numb!=None:
                        NameNumDic[name]=numb
    except:
        if not os.path.exists(NameListPath):#文件路径不存在
            with open(NameListPath,'wb') as f:
                pass
    return NameList,NameNumDic


def load_prefer_path(): #加载常用地址
    PreferPaths=[]
    path=app_path()+'/常用地址.hwa'
    try:
        with open(path) as f:
            if PreferPaths!=[]:
                PreferPaths=[]
            for line in f:
                if line[-1]=='\n' or line[-1]=='\r':
                    line = line[:-1]
                PreferPaths.append(line)
    except:
        if not os.path.exists(path):#文件路径不存在
            with open(path,'wb') as f:
                pass
    return PreferPaths


def find_name(name,NameList):#查询姓名
    PName=None
    for i in range(0,len(name)):
        if name[i:i+2] in NameList:
            PName = name[i:i+2]
            break
        elif name[i:i+3] in NameList:
            PName = name[i:i+3]
            break
    return PName





'''内部操作'''
def about_this_pro():
    about="本程序是由刘济伟因为懒得统计各种乱七八糟的作业情况而开发的\n如果你在里面发现了bug或者不足，请和刘济伟说一下。Thanks♪(･ω･)ﾉ"
    tkinter.messagebox.showinfo("关于本程序",about)


def help_():
    _help_="---开始使用---\n"
    _help_=_help_+"    1.在数据源中输入或者在下拉框中选择要统计的作业的文件夹的地址\n"
    _help_=_help_+"    2.单击开始统计以开始\n"
    _help_=_help_+"\n---更多用法帮助---\n"
    _help_=_help_+"    1.本程序在开始统计之后会每隔30秒更新一次作业情况,并在最下方显示更新时间和数据源\n"
    _help_=_help_+"    2.点击<保存到txt>按钮后，会将相关信息保存到\output文件夹中以 时间+被统计文件夹名 命名的文件里\n"
    _help_=_help_+"    3.当显示绿色\"正在统计\"时表示程序正常运行\n"
    _help_=_help_+"    4.点击<添加/删除常用数据源>可以添加/删除常用被统计文件夹，方便下次直接使用\n"
    _help_=_help_+"    5.如果出现了输入不规范等问题会弹出error提示框\n"
    _help_=_help_+"    6.点击保存学生名单后会将大文本框的内容保存到\"名单.hwa\"中"
    tkinter.messagebox.showinfo("帮助",_help_)


def update_contain():
    content='重构了代码并新增了自动发送邮件的功能'
    tkinter.messagebox.showinfo("更新内容",content)


UNKNOW_ERROR=0
FOLDER_NON_EXISTENT=1
INITIAL_LIST_EMPTY=2
LIST_LOAD_ERROR=3
EXCESSIVE_FILE_SIZE=4

def show_error(ErrorType):#输出错误信息
    """
    未知错误
    目标文件夹不存在
    初始名单为空
    加载名单出错
    """
    errors={} #[错误类型，可能原因]
    errors[0]=['error:未知错误','可能原因：\n目前未知的错误原因']
    errors[1]=['error:目标文件夹不存在','可能原因：\n数据源文件夹路径不存在或输入错误']
    errors[2]=['error:初始名单为空','可能原因：\n名单未添加内容']
    errors[3]=['error:加载名单出错','可能原因：\n名单存在问题']
    errors[4]=['error:文件过大','可能原因：发送的附件超过附件大小限制\n']
    errors[5]=['','可能原因：\n']
    errors[6]=['','可能原因：\n']
    errors[7]=['','可能原因：\n']
    errors[8]=['','可能原因：\n']
    errors[9]=['','可能原因：\n']
    errors[10]=['','可能原因：\n']
    tkinter.messagebox.showerror(errors[ErrorType][0],errors[ErrorType][1])


class Assignment_Manage:
    def __init__(self) -> None:
        """作业管理器初始化"""
        '''变量'''
        self.mode=IS_NOT_COUNTING
        self.NameList=[]
        self.FileName=''
        self.NameNumDic={}
        self.PreferPaths=[]
        '''初始化'''
        self.version='1.0.1'
        self.root=tk.Tk()
        self.root.title(f"电子版作业管理 v{self.version}")
        self.root.geometry('650x400')
        self.Load_Data()
        self.Menu_Init()
        self.Assembly_Init()#加载控件
        self.Load_Name_List()
        


    def Menu_Init(self):
        mainmenu=tk.Menu(self.root)
        # menuFile = tk.Menu(mainmenu)
        mainmenu.add_command(label='关于本程序',command=about_this_pro)
        mainmenu.add_command(label='帮助',command=help_)
        mainmenu.add_command(label='更新内容',command=update_contain)
        mainmenu.add_command(label='刷新名单',command=self.Load_Name_List)

        self.root.config(menu=mainmenu)#显示菜单


    def Assembly_Init(self):
        """控件初始化"""
        '''Frame'''

        '''标签'''
        self.Label_Source = tk.Label(self.root,text='数据源：',font=('黑体',15),width=8,height=1,anchor="w")
        self.Label_UHInformation = tk.Label(self.root,text='未交作业信息如下：',font=('黑体',15),anchor="w")
        self.Label_WhetherCounting = tk.Label(self.root,text='不在统计',fg='red',font=('黑体',15))
        self.Label_UpdateTime = tk.Label(self.root,text='上次数据更新时间：--:--:--',font=('黑体',15))

        '''输入框'''
        self.Combo_PathInput=tkinter.ttk.Combobox(self.root,font=('黑体',11),values=self.PreferPaths)
        try:
            self.Combo_PathInput.current(0)
        except:
            pass
        self.Combo_PathInput.bind('<<ComboboxSelected>>',self.Combo_Analyse)

        '''文本框'''
        self.Txt_InfoOutput = tk.Text(self.root,font=('黑体',15))
        self.Txt_Scroll = tk.Scrollbar(self.root)
        # 两个控件关联
        self.Txt_Scroll.config(command=self.Txt_InfoOutput.yview)
        self.Txt_InfoOutput.config(yscrollcommand=self.Txt_Scroll.set)

        '''按钮'''
        self.Button_WhetherCounting=tk.Button(self.root,text='开始统计',command=self.Button_Analyse)
        self.Button_SaveInfoTxtFile=tk.Button(self.root,text='保存到txt',command=self.Button_Save_Txt)
        self.Button_AddCommonSource=tk.Button(self.root,text='添加常用数据源',command=self.Button_Add_Source)
        self.Button_DelCommonSource=tk.Button(self.root,text='删除常用数据源',command=self.Button_Del_Source)
        self.Button_SaveStudentList=tk.Button(self.root,text='保存学生名单',command=self.Button_Add_NameList)
        self.Button_SendByEmail  =  tk.Button(self.root,text='一键发送作业',command=self.Button_Send_Email)
        
        '''布局'''
        self.Label_Source.place(x=10,y=10,height=20,width=90)
        self.Label_UHInformation.place(x=10,y=40,height=20,width=200)
        self.Label_WhetherCounting.place(x=400,y=160,height=40,width=100)
        self.Label_UpdateTime.place(x=10,y=340,height=40,width=350)
        self.Combo_PathInput.place(x=85,y=10,height=25,width=550)
        self.Txt_InfoOutput.place(x=10,y=70,height=270,width=350)
        self.Txt_Scroll.place(x=360,y=70,height=270,width=20)
        self.Button_WhetherCounting.place(x=400,y=200,height=40,width=100)
        self.Button_SaveInfoTxtFile.place(x=400,y=240,height=40,width=100)
        self.Button_AddCommonSource.place(x=400,y=40,height=40,width=100)
        self.Button_DelCommonSource.place(x=510,y=40,height=40,width=100)
        self.Button_SaveStudentList.place(x=400,y=300,height=40,width=100)
        self.Button_SendByEmail.place(x=510,y=100,height=40,width=100)


    def Run_App(self):
        """运行程序"""
        self.root.mainloop()

    
    def Load_Name_List(self):
        self.NameList,self.NameNumDic=load_name_list()


    def Load_Data(self):
        self.NameList,self.NameNumDic=load_name_list()
        self.PreferPaths=load_prefer_path()


    def Combo_Analyse(self,event):
        if self.mode==IS_COUNTING:
            self.mode=IS_NOT_COUNTING
            self.Button_Analyse()


    def Button_Analyse(self):
        if self.mode==IS_NOT_COUNTING:
            self.mode=IS_COUNTING
        else:
            self.mode=IS_NOT_COUNTING

        if self.mode==IS_NOT_COUNTING:
            self.Button_WhetherCounting['text']='开始统计'
            self.Label_WhetherCounting['text']='不在统计'
            self.Label_WhetherCounting['fg']='red'
        else:
            self.Button_WhetherCounting['text']='停止统计'
            self.Label_WhetherCounting['text']='正在统计'
            self.Label_WhetherCounting['fg']='green'
            self.Analyse()

    
    def Button_Save_Txt(self):
        FolderName,FolderPath=refine_FileName(self.Combo_PathInput.get())
        time=datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d-%H%M')
        TxtPath=app_path()+f'/output/{time}-{FolderName}.txt'

        if not os.path.exists(app_path()+'/output'):#文件路径不存在
            mkdir(app_path()+'/output')
        save_txt(TxtPath,self.Txt_InfoOutput.get('1.0','end'))


    def Button_Add_Source(self):
        if self.Combo_PathInput.get()!='' and self.Combo_PathInput.get() not in self.PreferPaths:
            self.PreferPaths.append(self.Combo_PathInput.get())
            path=app_path()+f'/常用地址.hwa'
            save_txt(path,'\n'.join(self.PreferPaths))
            self.Combo_PathInput['value']=self.PreferPaths

    
    def Button_Del_Source(self):
        if self.Combo_PathInput.get() in self.PreferPaths:
            self.PreferPaths.remove(self.Combo_PathInput.get())
            path=app_path()+f'/常用地址.hwa'
            save_txt(path,'\n'.join(self.PreferPaths))
            self.Combo_PathInput['value']=self.PreferPaths
    

    def Button_Add_NameList(self):
        """添加名单"""
        path=app_path()+'/名单.hwa'
        with open(path,'w') as f:
            f.write(self.Txt_InfoOutput.get('1.0','end'))
        self.Txt_InfoOutput.delete('1.0','end')


    def Button_Send_Email(self):
        """自动发送邮件的函数"""
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.header import Header
        from email.mime.base import MIMEBase
        mailserver = 'smtp.qq.com'#服务端
        userName_SendMail = '1357482552@qq.com'#发送者
        userName_AuthCode = 'fbbyofwzegeejbga'#授权码
        
        dir=self.Combo_PathInput.get()
        FolderName,FolderPath=refine_FileName(dir)
        WrongNames=[]
        for FilePath in os.listdir(dir):
            Name=find_name(FilePath,self.NameList)
            received_mail=f'{self.NameNumDic[Name]}@smbu.edu.cn'
            
            # 编辑邮件信息
            email = MIMEMultipart()
            email['Subject'] = f'{Name}的作业'  # 定义邮件主题
            email['From'] = userName_SendMail  # 发件人
            email['To'] = received_mail  # 收件人（可以添加多个，若只有一个收件人，可直接写邮箱号）

            # 正文
            content=f'这是{FolderName}，请查收。'
            email.attach(MIMEText(content,'plain','utf-8'))

            # 附件
            att = MIMEText(open(f'{FolderPath}/{FilePath}', 'rb').read(), 'base64', 'gbk')
            att["Content-Type"] = 'application/octet-stream'
            att.add_header('Content-Disposition','attachment',filename=('gbk','',f'{Name}的作业.pdf'))
            email.attach(att)

            try:
                smtp = smtplib.SMTP_SSL(mailserver, port=465)
                smtp.login(userName_SendMail, userName_AuthCode)
                smtp.sendmail(userName_SendMail, received_mail, email.as_string())
                smtp.quit()
                print(f'{Name}的作业 已发送')
            except:
                WrongNames.append(Name)
                print(f'{Name}的作业 发送失败~')
        # print('作业已发送完毕')
        if len(WrongNames)==0:
            tkinter.messagebox.showinfo('自动发送作业','作业已发送完毕\n全部发送成功！！！')
        else:
            WrongNamesTxt='\n'.join(WrongNames)
            tkinter.messagebox.showinfo('自动发送作业',f'作业已发送完毕\n以下同学的作业发送失败:\n{WrongNamesTxt}')


    def Analyse(self):
        RuntimeLimit=5
        flag=True
        ErrorShow = False 
        MultiUp=False
        runtime=0
        self.Txt_InfoOutput.delete('1.0','end')

        if self.NameList==[]:#无名单
            load_name_list()

        while flag and runtime<RuntimeLimit:
            try:
                UnList = self.NameList.copy()
                FileName,dir=refine_FileName(self.Combo_PathInput.get())#获取文件夹名和文件夹路径

                if not os.path.exists(dir):#文件路径不存在
                    show_error(FOLDER_NON_EXISTENT)
                    self.Button_Analyse()
                    break

                if self.NameList==[]:#无名单
                    show_error(INITIAL_LIST_EMPTY)
                    self.Button_Analyse()
                    break

                for name in os.listdir(dir):#输出未交名单
                    PName = find_name(name,self.NameList)
                    if PName==None:
                        continue
                    if PName in UnList:
                        UnList.remove(PName)
                    else:#有重复文件的警告
                        MultiUp=True
                if MultiUp:
                    self.Txt_InfoOutput.insert('end',"\n\n警告：有重复提交的作业\n\n\n")
                self.Txt_InfoOutput.insert('end',f"{FileName}未交作业名单({len(UnList)}人)：\n")
                self.Txt_InfoOutput.insert('end','\n'.join(UnList))
                timestr='上次数据更新时间：'+datetime.datetime.strftime(datetime.datetime.now(),'%H:%M:%S')
                self.Label_UpdateTime['text']=timestr+"\n数据源："+refine_FileName(self.Combo_PathInput.get())[0]
            except:
                runtime+=1
                time.sleep(1)
                continue
            else:
                flag=False

        if runtime>=RuntimeLimit:
            self.Button_Analyse()
            if not ErrorShow:
                show_error(0)
        
        if self.mode==IS_COUNTING:
            self.root.after(30000,self.Analyse)
            # root.after(5000,analyse)


    def blank_func(self):
        """空函数，未开发完的按钮等控件使用"""
        pass


AssignmentManage=Assignment_Manage()
AssignmentManage.Run_App()
