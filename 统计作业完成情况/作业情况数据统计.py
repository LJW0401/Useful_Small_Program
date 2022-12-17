import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import os
import datetime
import time
import os.path

def app_path():
    import sys
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)            #没打包前的py目录


'''全局变量'''
analysis=False
NameList=[]
FileName=''
NameNumDic={}
#UnhandNameList=[]
PreferPaths=[]


'''函数开发'''
def show_error(ErrorType):#输出错误信息
    """
    0:未知错误
    1:目标文件夹不存在
    2:初始名单为空
    3:
    4:
    5:
    6:
    7:
    8:
    9:
    10:
    """
    errors={} #[错误类型，可能原因]
    errors[0]=['error:未知错误','可能原因：\n目前未知的错误原因']
    errors[1]=['error:目标文件夹不存在','可能原因：\n数据源文件夹路径不存在或输入错误']
    errors[2]=['error:初始名单为空','可能原因：\n名单未添加内容']
    errors[3]=['error:加载名单出错','可能原因：\n名单存在问题']
    errors[4]=['','可能原因：\n']
    errors[5]=['','可能原因：\n']
    errors[6]=['','可能原因：\n']
    errors[7]=['','可能原因：\n']
    errors[8]=['','可能原因：\n']
    errors[9]=['','可能原因：\n']
    errors[10]=['','可能原因：\n']
    tkinter.messagebox.showerror(errors[ErrorType][0],errors[ErrorType][1])



def mkdir(path):#创建文件夹目录
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)



def save_txt(path,txt):
    with open(path,'w') as f:
        f.write(txt)


def refine_FileName(FilePath:str):#提取文件夹的名字并返回合适格式的文件路径
    file_splited=FilePath.split('\\')
    FileName=file_splited[-1]
    
    return FileName , '/'.join(file_splited)


def load_name_list():#加载名单信息
    global NameList
    NameListPath=app_path()+'/名单.hwa'
    try:
        with open(NameListPath) as f:
            
            if NameList!=[]:
                NameList=[]

            for line in f:
                if line[-1]=='\n' or line[-1]=='\r':
                    line = line[:-1]
                list_=line.split('\t')
                # if len(list_)==1:
                #     NameList.append(list_[0])
                #     continue
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



def load_prefer_path(): #加载常用地址
    global PreferPaths
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
    #print(PreferPaths)


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


def find_numb(name,NameList):#查询学号
    
    return 


def analyse():#分析未交作业的情况
    global analysis,FileName,NameList
    RuntimeLimit=5
    flag=True
    ErrorShow = False 
    MultiUp=False
    runtime=0
    #print('analysing')
    txt1.delete('1.0','end')

    if NameList==[]:#无名单
        load_name_list()

    while flag and runtime<RuntimeLimit:
        #print('trying')
        try:
            UnList = NameList.copy()
            FileName,dir=refine_FileName(entry1.get())#获取文件夹名和文件夹路径

            if not os.path.exists(dir):#文件路径不存在
                show_error(1)
                button_analyse()
                break
            
            if NameList==[]:#无名单
                show_error(2)
                button_analyse()
                break

            for name in os.listdir(dir):#输出未交名单
                PName = find_name(name,NameList)
                if PName==None:
                    continue
                if PName in UnList:
                    UnList.remove(PName)
                else:#有重复文件的警告
                    MultiUp=True
            if MultiUp:
                txt1.insert('end',"\n\n警告：有重复提交的作业\n\n\n")
            txt1.insert('end',f"{FileName}未交作业名单({len(UnList)}人)：\n")
            txt1.insert('end','\n'.join(UnList))
            timestr='上次数据更新时间：'+datetime.datetime.strftime(datetime.datetime.now(),'%H:%M:%S')
            label4['text']=timestr+"\n数据源："+refine_FileName(entry1.get())[0]
        except:
            runtime+=1
            time.sleep(1)
            continue
        else:
            flag=False

    if runtime>=RuntimeLimit:
        button_analyse()
        if not ErrorShow:
            show_error(0)
    
    if analysis:
        root.after(30000,analyse)
        # root.after(5000,analyse)
    

def button_analyse():
    global analysis
    analysis=not analysis
    if not analysis:
        button1['text']='开始统计'
        label3['text']='不在统计'
        label3['fg']='red'
    else:
        button1['text']='停止统计'
        label3['text']='正在统计'
        label3['fg']='green'
        analyse()
        


def button_save_txt():
    #tkinter.messagebox.showerror("error",'功能暂且不可用')
    #return
    global FileName
    time=datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d-%H%M')
    TxtPath=app_path()+f'/output/{time}-{FileName}.txt'

    if not os.path.exists(app_path()+'/output'):#文件路径不存在
        mkdir(app_path()+'/output')

    save_txt(TxtPath,txt1.get('1.0','end'))


def button_add_source():
    global PreferPaths
    if entry1.get()!='' and entry1.get() not in PreferPaths:
        PreferPaths.append(entry1.get())
        path=app_path()+f'/常用地址.hwa'
        save_txt(path,'\n'.join(PreferPaths))
        entry1['value']=PreferPaths


def button_del_source():
    global PreferPaths
    if entry1.get() in PreferPaths:
        PreferPaths.remove(entry1.get())
        path=app_path()+f'/常用地址.hwa'
        save_txt(path,'\n'.join(PreferPaths))
        entry1['value']=PreferPaths


def button_add_NameList():
    path=app_path()+'/名单.hwa'
    with open(path,'w') as f:
        f.write(txt1.get('1.0','end'))
    txt1.delete('1.0','end')


def combo_analyse(event):
    global analysis
    if analysis:
        analysis=False
        button_analyse()


def load_data():
    load_name_list()
    load_prefer_path()


#init_windows
'''窗口初始化'''
root = tk.Tk()
root.title('同学作业情况数据统计 v1.1.9')
root.geometry('400x400') # 这里的乘号不是 * ，而是小写英文字母 x



'''数据加载'''

load_data()



'''菜单开发区域'''
def blank_func():
    pass

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
    contain='懒得写了'
    tkinter.messagebox.showinfo("更新内容",contain)


mainmenu=tk.Menu(root)
menuFile = tk.Menu(mainmenu)
mainmenu.add_command(label='关于本程序',command=about_this_pro)
mainmenu.add_command(label='帮助',command=help_)
mainmenu.add_command(label='更新内容',command=update_contain)
mainmenu.add_command(label='刷新名单',command=load_name_list)

root.config(menu=mainmenu)#显示菜单




'''标签控件区域'''
label1 = tk.Label(root,text='数据源：',
        #bg='#d3fbfb',
        #fg='red',
        font=('黑体',15),
        width=8,
        height=1,
        anchor="w")
#label1.place(relx=0.5,y=80,relheight=0.4,width=200)
label1.place(x=10,y=10,height=20,width=90)

label2 = tk.Label(root,text='未交作业信息如下：',font=('黑体',15),anchor="w")
label2.place(x=10,y=40,height=20,width=200)

label3 = tk.Label(root,text='不在统计',fg='red',font=('黑体',15))
label3.place(x=290,y=160,height=40,width=100)

label4 = tk.Label(root,text='上次数据更新时间：--:--:--',font=('黑体',15))
label4.place(x=25,y=340,height=40,width=350)



'''输入框控件区域'''
# entry1=tk.Entry(root,
#         font=('黑体',15),
#         width=10)
entry1=tkinter.ttk.Combobox(root,font=('黑体',11),values=PreferPaths)
entry1.place(x=85,y=10,height=25,width=300)
try:
    entry1.current(0)
except:
    pass
entry1.bind('<<ComboboxSelected>>',combo_analyse)


'''输出框展示区域'''
txt1 = tk.Text(root,font=('黑体',15))
txt1.place(x=10,y=70,height=270,width=250)
scroll_1 = tk.Scrollbar()
scroll_1.place(x=260,y=70,height=270,width=20)
# 两个控件关联
scroll_1.config(command=txt1.yview)
txt1.config(yscrollcommand=scroll_1.set)



'''按钮展示区域'''
button1=tk.Button(root,text='开始统计',command=button_analyse)
button1.place(x=290,y=200,height=40,width=100)

button2=tk.Button(root,text='保存到txt',command=button_save_txt)
button2.place(x=290,y=240,height=40,width=100)

button3=tk.Button(root,text='添加常用数据源',command=button_add_source)
button3.place(x=290,y=40,height=40,width=100)

button4=tk.Button(root,text='删除常用数据源',command=button_del_source)
button4.place(x=290,y=80,height=40,width=100)

button5=tk.Button(root,text='保存学生名单',command=button_add_NameList)
button5.place(x=290,y=300,height=40,width=100)


'''运行过程'''




'''维持窗口'''
root.mainloop()