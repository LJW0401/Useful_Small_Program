import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import os
import datetime as dt
import time
import os.path
import pandas as pd
'''常量'''
START_YEAR=2022
FINISH_YEAR=2050

DOING = 0
DONE = 1

TOTALLY_IN=0
PARTLY_IN_SINGLE=1
PARTLY_IN_MULTIPLE=2
TOTALLY_NOT_IN=3
TOTALLY_COVER=4

SAVE_INTERVAL=60000 #1m=60s=60000ms
REPETITION_FREQUENCY_LIST=['不重复','每天','每周','每月','每年']
NONE=0
DAYLY=1
WEEKLY=2
MONTHLY=3
ANNUALY=4
REPETITION_FREQUENCY_MODE={'不重复':NONE,'每天':DAYLY,'每周':WEEKLY,'每月':MONTHLY,'每年':ANNUALY}
DATETIME_STR_DEMO="%Y/%m/%d %H:%M"


'''基本操作'''
def App_path():
    import sys
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)            #没打包前的py目录


'''相关函数'''
def Fix_number_of_day(Year:int,Month:int):
    if Month in [1,3,5,7,8,10,12]:
        return [i for i in range(1,32)]
    elif Month in [4,6,9,11]:
        return [i for i in range(1,31)]
    elif Month==2 and (Year%4==0 and Year%100!=0 or Year%400==0):
        return [i for i in range(1,30)]
    elif Month==2 and not(Year%4==0 and Year%100!=0 or Year%400==0):
        return [i for i in range(1,29)]
    else:
        return None



'''相关的类'''
#带滚动条的Frame
class ScrollbarFrame:
    def __init__(self,master,width,height) -> None:
        self.canvas=tk.Canvas(master,width=width,height=height,bg='black') #创建canvas
        self.scrollbar=tk.Scrollbar(self.canvas,command=self.canvas.yview) #竖直滚动条
        self.frame=tk.Frame(self.canvas) #把frame放在canvas里
        self.frame.place(x=0,y=0,width=width, height=height) #frame的长宽，和canvas差不多的
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0,0), window=self.frame)  #create_window
        self.canvas.configure(yscrollcommand=self.scrollbar.set) #设置  
        self.canvas.place(x = 0, y = 0) #放置canvas的位置
        self.scrollbar.place(x = width-18,y=2,width=width,height=height)
        
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)  # 绑定鼠标滚轮
        self.frame.bind("<MouseWheel>", self.on_mousewheel)  # 绑定鼠标滚轮

    def on_mousewheel(self,event):  # 鼠标滚轮
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def place(self,**kwargs):
        x=kwargs.get('x') if kwargs.get('x')!=None else self.canvas.place_info()['x']
        y=kwargs.get('y') if kwargs.get('y')!=None else self.canvas.place_info()['y']
        height=kwargs.get('height') if kwargs.get('height')!=None else self.canvas.place_info()['height']
        width=kwargs.get('width') if kwargs.get('width')!=None else self.canvas.place_info()['width']
        self.canvas.place(x=x,y=y,height=height,width=width)


#在Checkbutton中添加一些信息和函数
class Checkbutton(tk.Checkbutton):
    def __init__(self, container,TaskInfo, *args, **kwargs):
        super().__init__(container,*args, **kwargs)
        self.TaskInfo=TaskInfo
    
    
    # def 

'''定义软件的类'''
class Task_Manage:
    def __init__(self) -> None:
        """初始化类"""
        self.version='1.0.4'
        self.TaskDataFrame=None
        self.change=False
        self.NowTime=None
        self.TaskCheckButtons=[]


# 初始化的函数
    def App_init(self):
        """程序初始化"""
        self.root=tk.Tk()
        self.root.title(f"任务管理器 v{self.version}")
        self.root.geometry('650x500')


    def Assembly_init(self):
        """控件初始化"""
#控件初始化及布局
# 显示系统时间
        self.Label_NowTime=tk.Label(
            self.root,
            text='现在系统时间 ----/--/-- --:--:--',
            font=('黑体',15),
            # anchor='w'
        )
        self.Label_NowTime.pack(side='top',anchor='w')

# 选择具体时间
        Frame_ChooseDate=tk.Frame(self.root)
        Frame_ChooseDate.pack(side='top',anchor='w')

        Label_ChooseDate=tk.Label(
            Frame_ChooseDate,
            text='选择日期：',
            anchor="w"
        )
        Label_ChooseDate.pack(side='left')

        self.Combo_ChooseDate_Year=tkinter.ttk.Combobox(
            Frame_ChooseDate,
            values=[i for i in range(START_YEAR,FINISH_YEAR+1)],
            width=4
        )
        self.Combo_ChooseDate_Year.current(0)
        self.Combo_ChooseDate_Year.pack(side='left')

        self.Combo_ChooseDate_Month=tkinter.ttk.Combobox(
            Frame_ChooseDate,
            values=[i for i in range(1,13)],
            width=2
        )
        self.Combo_ChooseDate_Month.current(0)
        self.Combo_ChooseDate_Month.pack(side='left',padx=5)

        self.Combo_ChooseDate_Day=tkinter.ttk.Combobox(
            Frame_ChooseDate,
            values=[i for i in range(1,32)],
            width=2
        )
        self.Combo_ChooseDate_Day.current(0)
        self.Combo_ChooseDate_Day.pack(side='left')

        self.Combo_ChooseDate_Month.bind('<<ComboboxSelected>>',self.Fix_number_of_day_ChooseDate)

# 显示当前应做的任务
        self.Frame_NowTask=tk.LabelFrame(
            self.root,
            text='当前任务',
            height=100,
            width=100
        )
        self.Frame_NowTask.pack(side='top',anchor='w',padx=5)




# 添加新任务
        self.Frame_AddTask=tk.LabelFrame(
            self.root,
            text='添加新任务',
            relief='groove',bd=1
        )
        self.Frame_AddTask.pack(side='top',anchor='w',padx=5)
        
    # 添加新任务名
        Frame_NewTaskName=tk.Frame(
            self.Frame_AddTask,
            relief='groove',bd=1
        )
        Frame_NewTaskName.pack(side='top',fill='x',padx=5,ipady=3)

        Label_NewTaskName=tk.Label(
            Frame_NewTaskName,
            text='任务名：  ',
            anchor="w"
        )
        Label_NewTaskName.pack(side='left')
        
        self.Entry_NewTaskName=tk.Entry(Frame_NewTaskName)
        self.Entry_NewTaskName.pack(side='left',expand='yes')

    # 添加开始日期
        Frame_NewTaskStartTime=tk.Frame(
            self.Frame_AddTask,
            relief='groove',bd=1
        )
        Frame_NewTaskStartTime.pack(side='top',fill='x',padx=5,ipady=3)

        Label_NewTaskStartTime=tk.Label(
            Frame_NewTaskStartTime,
            text='开始时间：',
            anchor='w'
        )
        Label_NewTaskStartTime.pack(side='left')
        #开始日期的年份
        self.Combo_NewTaskStartTime_Year=tkinter.ttk.Combobox(
            Frame_NewTaskStartTime,
            values=[i for i in range(START_YEAR,FINISH_YEAR+1)],
            width=4
        )
        self.Combo_NewTaskStartTime_Year.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)
        self.Combo_NewTaskStartTime_Year.current(0)
        self.Combo_NewTaskStartTime_Year.pack(side='left')
        #开始日期的月份
        self.Combo_NewTaskStartTime_Month=tkinter.ttk.Combobox(
            Frame_NewTaskStartTime,
            values=[i for i in range(1,13)],
            width=2
        )
        self.Combo_NewTaskStartTime_Month.bind('<<ComboboxSelected>>',self.Fix_number_of_day_StartTime)
        self.Combo_NewTaskStartTime_Month.current(0)
        self.Combo_NewTaskStartTime_Month.pack(side='left',padx=5)
        #开始日期的日期
        self.Combo_NewTaskStartTime_Day=tkinter.ttk.Combobox(
            Frame_NewTaskStartTime,
            values=[i for i in range(1,32)],
            width=2
        )
        self.Combo_NewTaskStartTime_Day.current(0)
        self.Combo_NewTaskStartTime_Day.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)
        self.Combo_NewTaskStartTime_Day.pack(side='left')
        #开始日期的小时
        self.Combo_NewTaskStartTime_Hour=tkinter.ttk.Combobox(
            Frame_NewTaskStartTime,
            values=[i for i in range(0,24)],
            width=2
        )
        self.Combo_NewTaskStartTime_Hour.current(0)
        self.Combo_NewTaskStartTime_Hour.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)
        self.Combo_NewTaskStartTime_Hour.pack(side='left',padx=5)
        #开始日期的分钟
        self.Combo_NewTaskStartTime_Minute=tkinter.ttk.Combobox(
            Frame_NewTaskStartTime,
            values=[i for i in range(0,60)],
            width=2
        )
        self.Combo_NewTaskStartTime_Minute.current(0)
        self.Combo_NewTaskStartTime_Minute.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)
        self.Combo_NewTaskStartTime_Minute.pack(side='left')
    #输入框重新排布
        self.Entry_NewTaskName.pack(side='left',fill='x')

    # 添加截止日期
        Frame_NewTaskDeadLine=tk.Frame(
            self.Frame_AddTask,
            relief='groove',bd=1
        )
        Frame_NewTaskDeadLine.pack(side='top',fill='x',padx=5,ipady=3)

        Label_NewTaskDeadLine=tk.Label(
            Frame_NewTaskDeadLine,
            text='截止时间：',
            anchor='w'
        )
        Label_NewTaskDeadLine.pack(side='left')
        #截止日期的年份
        self.Combo_NewTaskDeadLine_Year=tkinter.ttk.Combobox(
            Frame_NewTaskDeadLine,
            values=[i for i in range(START_YEAR,FINISH_YEAR+1)],
            width=4
        )
        self.Combo_NewTaskDeadLine_Year.current(0)
        self.Combo_NewTaskDeadLine_Year.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        self.Combo_NewTaskDeadLine_Year.pack(side='left')
        #截止日期的月份
        self.Combo_NewTaskDeadLine_Month=tkinter.ttk.Combobox(
            Frame_NewTaskDeadLine,
            values=[i for i in range(1,13)],
            width=2
        )
        self.Combo_NewTaskDeadLine_Month.current(0)
        self.Combo_NewTaskDeadLine_Month.bind('<<ComboboxSelected>>',self.Fix_number_of_day_DeadLine)
        self.Combo_NewTaskDeadLine_Month.pack(side='left',padx=5)
        #截止日期的日期
        self.Combo_NewTaskDeadLine_Day=tkinter.ttk.Combobox(
            Frame_NewTaskDeadLine,
            values=[i for i in range(1,32)],
            width=2
        )
        self.Combo_NewTaskDeadLine_Day.current(0)
        self.Combo_NewTaskDeadLine_Day.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        self.Combo_NewTaskDeadLine_Day.pack(side='left')
        #截止日期的小时
        self.Combo_NewTaskDeadLine_Hour=tkinter.ttk.Combobox(
            Frame_NewTaskDeadLine,
            values=[i for i in range(0,24)],
            width=2
        )
        self.Combo_NewTaskDeadLine_Hour.current(0)
        self.Combo_NewTaskDeadLine_Hour.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        self.Combo_NewTaskDeadLine_Hour.pack(side='left',padx=5)
        #截止日期的分钟
        self.Combo_NewTaskDeadLine_Minute=tkinter.ttk.Combobox(
            Frame_NewTaskDeadLine,
            values=[i for i in range(0,60)],
            width=2
        )
        self.Combo_NewTaskDeadLine_Minute.current(0)
        self.Combo_NewTaskDeadLine_Minute.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        self.Combo_NewTaskDeadLine_Minute.pack(side='left')

    # 添加备注
        Frame_NewTaskNotes=tk.Frame(
            self.Frame_AddTask,
            relief='groove',bd=1
        )
        Frame_NewTaskNotes.pack(side='top',fill='x',padx=5,ipady=3)

        Label_NewTaskNotes=tk.Label(
            Frame_NewTaskNotes,
            text='任务备注：',
            anchor='w'
        )
        Label_NewTaskNotes.pack(side='left')
        #创建一个区域来放置文本框及滚动条
        Frame_NewTaskNotes_ST=tk.Frame(
            Frame_NewTaskNotes,
            relief='groove',bd=1
        )
        Frame_NewTaskNotes_ST.pack(side='left',fill='x')
        # 创建文本框及滚动条
        self.Txt_NewTaskNotes = tk.Text(
            Frame_NewTaskNotes_ST,
            height=4,
            width=30
        )
        self.Txt_NewTaskNotes.pack(side='left',expand='no',anchor='w')
        self.Txt_NewTaskNotes_yScroll = tk.Scrollbar(Frame_NewTaskNotes_ST)
        self.Txt_NewTaskNotes_yScroll.pack(side='right',fill='y')
        # 两个控件关联
        self.Txt_NewTaskNotes_yScroll.config(command=self.Txt_NewTaskNotes.yview)
        self.Txt_NewTaskNotes.config(yscrollcommand=self.Txt_NewTaskNotes_yScroll.set)
        
    # 重复频率
        Frame_NewTaskRepetitionFrequency=tk.Frame(
            self.Frame_AddTask,
            relief='groove',bd=1
        )
        Frame_NewTaskRepetitionFrequency.pack(side='top',fill='x',padx=5,ipady=3)

        Label_NewTaskRepetitionFrequency=tk.Label(
            Frame_NewTaskRepetitionFrequency,
            text='重复频率：',
            anchor='w'
        )
        Label_NewTaskRepetitionFrequency.pack(side='left')
        self.Combo_NewTaskRepetitionFrequency=tkinter.ttk.Combobox(
            Frame_NewTaskRepetitionFrequency,
            values=REPETITION_FREQUENCY_LIST[:3],
            width=6
        )
        self.Combo_NewTaskRepetitionFrequency.current(0)
        self.Combo_NewTaskRepetitionFrequency.pack(side='left')
        
        Label_NewTaskRepetitionTimes=tk.Label(
            Frame_NewTaskRepetitionFrequency,
            text='       重复次数：',
            anchor='w'
        )
        Label_NewTaskRepetitionTimes.pack(side='left')
        self.Entry_NewTaskRepetitionTimes=tk.Entry(
            Frame_NewTaskRepetitionFrequency,
            width=10
        )
        self.Entry_NewTaskRepetitionTimes.pack(side='left')

    # 优先级
        Frame_NewTaskPriority=tk.Frame(
            self.Frame_AddTask,
            relief='groove',bd=1
        )
        Frame_NewTaskPriority.pack(side='top',fill='x',padx=5,ipady=3)

        Label_NewTaskPriority=tk.Label(Frame_NewTaskPriority,text='优先级：',anchor='w')
        Label_NewTaskPriority.pack(side='left')

        self.Combo_NewTaskPriority=tkinter.ttk.Combobox(
            Frame_NewTaskPriority,
            values=[i for i in range(0,5)],
            width=2
        )
        self.Combo_NewTaskPriority.current(0)
        self.Combo_NewTaskPriority.pack(side='left')
    # 添加新任务按钮，与优先级在同一行中
        self.Button_AddNewTask=tk.Button(
            Frame_NewTaskPriority,
            text='添加新任务',
            command=self.Button_Add_new_task
        )
        self.Button_AddNewTask.pack(side='right')
        

    def Files_check(self):
        """文件完整性检测"""
        try:
            self.TaskDataFrame=pd.read_excel(f'{App_path()}/Tasks.xlsx',sheet_name=0)
        except:
            dic={'任务名':[],
                '优先级' :[],
                '开始时间':[],
                '截止时间':[],
                '完成情况':[],
                '备注':[]}
            self.TaskDataFrame=pd.DataFrame(dic)
            self.change=True
        self.Save_file()
        self.Show_data_frame()
    

    def Parameter_correct(self):
        """校准参数"""
        #开始日期确定为当前时间
        NowTime = dt.datetime.now()
        NowYear=int(NowTime.strftime("%Y"))
        NowMonth=int(NowTime.strftime("%m"))
        NowDay=int(NowTime.strftime("%d"))
        NowHour=int(NowTime.strftime("%H"))
        NowMinute=int(NowTime.strftime("%M"))

        self.Combo_NewTaskStartTime_Year.current(NowYear-START_YEAR)
        self.Combo_NewTaskStartTime_Month.current(NowMonth-1)
        self.Combo_NewTaskStartTime_Day.current(NowDay-1)
        self.Combo_NewTaskStartTime_Hour.current(NowHour)
        self.Combo_NewTaskStartTime_Minute.current(NowMinute)

        self.Combo_NewTaskDeadLine_Year.current(NowYear-START_YEAR)
        self.Combo_NewTaskDeadLine_Month.current(NowMonth-1)
        self.Combo_NewTaskDeadLine_Day.current(NowDay-1)
        self.Combo_NewTaskDeadLine_Hour.current(NowHour)
        self.Combo_NewTaskDeadLine_Minute.current(NowMinute)

        self.Combo_ChooseDate_Year.current(NowYear-START_YEAR)
        self.Combo_ChooseDate_Month.current(NowMonth-1)
        self.Combo_ChooseDate_Day.current(NowDay-1)
        # print(NowTime)
        # print(NowYear,NowMonth,NowDay,NowHour,NowMinute,NowTime.strftime("%f"))

        # 更新当前时间
        self.Update_time()


# 具体的控件功能函数
    def Present_Tasks(self):
        """展示任务"""
        pass


    def Button_Add_new_task(self):
        NewTaskName=self.Entry_NewTaskName.get()
        if NewTaskName=='':
            tkinter.messagebox.showerror('输入错误','缺少任务名')
            return
        year=  int(self.Combo_NewTaskStartTime_Year.get())
        month= int(self.Combo_NewTaskStartTime_Month.get())
        day=   int(self.Combo_NewTaskStartTime_Day.get())
        hour=  int(self.Combo_NewTaskStartTime_Hour.get())
        minute=int(self.Combo_NewTaskStartTime_Minute.get())
        NewTaskStartTime=dt.datetime(year,month,day,hour,minute)

        year=  int(self.Combo_NewTaskDeadLine_Year.get())
        month= int(self.Combo_NewTaskDeadLine_Month.get())
        day=   int(self.Combo_NewTaskDeadLine_Day.get())
        hour=  int(self.Combo_NewTaskDeadLine_Hour.get())
        minute=int(self.Combo_NewTaskDeadLine_Minute.get())
        NewTaskDeadLine=dt.datetime(year,month,day,hour,minute)

        NewTaskPriority=int(self.Combo_NewTaskPriority.get())
        NewTaskNotes=self.Txt_NewTaskNotes.get('1.0','end')
        NewTaskRepetitionFrequencyMode=REPETITION_FREQUENCY_MODE[self.Combo_NewTaskRepetitionFrequency.get()]
        
        if NewTaskRepetitionFrequencyMode==NONE:
            DeltaTime=dt.timedelta(days=0)
        elif NewTaskRepetitionFrequencyMode==DAYLY:
            DeltaTime=dt.timedelta(days=1)
        elif NewTaskRepetitionFrequencyMode==WEEKLY:
            DeltaTime=dt.timedelta(weeks=1)
        elif NewTaskRepetitionFrequencyMode==MONTHLY:
            tkinter.messagebox.showwarning('待开发','尚不支持每月规划')
            return
            DeltaTime=dt.timedelta(weeks=1)
        elif NewTaskRepetitionFrequencyMode==ANNUALY:
            tkinter.messagebox.showwarning('待开发','尚不支持每年规划')
            return

        if NewTaskRepetitionFrequencyMode==NONE:
            NewTaskRepetitionTime=1
        elif self.Entry_NewTaskRepetitionTimes.get()!='':
            try:
                NewTaskRepetitionTime=int(self.Entry_NewTaskRepetitionTimes.get())
            except:
                tkinter.messagebox.showerror('输入错误','请在重复次数中输入数字')
        else:
            NewTaskRepetitionTime=1
# 还要做一个去重功能
        # EqualNameTaskDataFrame=self.TaskDataFrame[self.TaskDataFrame['任务名']==NewTaskName]
        for _ in range(NewTaskRepetitionTime):
            NewTaskInfoDict={
                    '任务名':NewTaskName,
                    '优先级' :NewTaskPriority,
                    '开始时间':NewTaskStartTime.strftime(DATETIME_STR_DEMO),
                    '截止时间':NewTaskDeadLine.strftime(DATETIME_STR_DEMO),
                    '完成情况':DOING,
                    '备注':NewTaskNotes}

            InTaskMode,Rows=self.NewTask_In_Tasks(NewTaskInfoDict)

            if InTaskMode==TOTALLY_IN:
                pass #直接进入到下一循环中
            elif InTaskMode==TOTALLY_NOT_IN:
                self.TaskDataFrame.loc[self.TaskDataFrame.index.size]=NewTaskInfoDict
                self.change=True
            elif InTaskMode==PARTLY_IN_SINGLE:
                pass
            elif InTaskMode==PARTLY_IN_MULTIPLE:
                pass

            NewTaskStartTime=NewTaskStartTime+DeltaTime
            NewTaskDeadLine= NewTaskDeadLine +DeltaTime

        self.Show_data_frame()
        self.Save_file()
        

    def Fix_number_of_day_ChooseDate(self,event=None):
        """确定选择的日期的天数"""
        Year=int(self.Combo_ChooseDate_Year.get())
        Month=int(self.Combo_ChooseDate_Month.get())
        Days=Fix_number_of_day(Year,Month)
        if Days==None:
            tkinter.messagebox.showerror('输入错误','输入的月份不合法')
        else:
            self.Combo_NewTaskStartTime_Day['value']=Days


    def Fix_number_of_day_StartTime(self,event=None):
        """确定开始日期天数"""
        Year=int(self.Combo_NewTaskStartTime_Year.get())
        Month=int(self.Combo_NewTaskStartTime_Month.get())
        Days=Fix_number_of_day(Year,Month)
        if Days==None:
            tkinter.messagebox.showerror('输入错误','输入的月份不合法')
        else:
            self.Combo_NewTaskStartTime_Day['value']=Days
        """然后确保截止时间>开始时间"""
        self.Click_StartTime_ensure_DeadLine()
            

    def Fix_number_of_day_DeadLine(self,event=None):
        """确定截止日期天数"""
        Year=int(self.Combo_NewTaskDeadLine_Year.get())
        Month=int(self.Combo_NewTaskDeadLine_Month.get())
        Days=Fix_number_of_day(Year,Month)
        if Days==None:
            tkinter.messagebox.showerror('输入错误','输入的月份不合法')
        else:
            self.Combo_NewTaskDeadLine_Day['value']=Days
        """然后确保截止时间>开始时间"""
        self.Click_DeadLine_ensure_StartTime()
        

    def Click_StartTime_ensure_DeadLine(self,event=None):
        """确保截止时间>开始时间"""
        if int(self.Combo_NewTaskStartTime_Year.get())>int(self.Combo_NewTaskDeadLine_Year.get()):
            self.Combo_NewTaskDeadLine_Year.current(int(self.Combo_NewTaskStartTime_Year.get())-START_YEAR)
        elif int(self.Combo_NewTaskStartTime_Year.get())<int(self.Combo_NewTaskDeadLine_Year.get()):
            return
        
        if int(self.Combo_NewTaskStartTime_Month.get())>int(self.Combo_NewTaskDeadLine_Month.get()):
            self.Combo_NewTaskDeadLine_Month.current(int(self.Combo_NewTaskStartTime_Month.get())-1)
        elif int(self.Combo_NewTaskStartTime_Month.get())<int(self.Combo_NewTaskDeadLine_Month.get()):
            return

        if int(self.Combo_NewTaskStartTime_Day.get())>int(self.Combo_NewTaskDeadLine_Day.get()):
            self.Combo_NewTaskDeadLine_Day.current(int(self.Combo_NewTaskStartTime_Day.get())-1)
        elif int(self.Combo_NewTaskStartTime_Day.get())<int(self.Combo_NewTaskDeadLine_Day.get()):
            return

        if int(self.Combo_NewTaskStartTime_Hour.get())>int(self.Combo_NewTaskDeadLine_Hour.get()):
            self.Combo_NewTaskDeadLine_Hour.current(int(self.Combo_NewTaskStartTime_Hour.get()))
        elif int(self.Combo_NewTaskStartTime_Hour.get())<int(self.Combo_NewTaskDeadLine_Hour.get()):
            return
        
        if int(self.Combo_NewTaskStartTime_Minute.get())>int(self.Combo_NewTaskDeadLine_Minute.get()):
            self.Combo_NewTaskDeadLine_Minute.current(int(self.Combo_NewTaskStartTime_Minute.get()))
    
    
    def Click_DeadLine_ensure_StartTime(self,event=None):
        """确保截止时间>开始时间"""
        if int(self.Combo_NewTaskStartTime_Year.get())>int(self.Combo_NewTaskDeadLine_Year.get()):
            self.Combo_NewTaskStartTime_Year.current(int(self.Combo_NewTaskDeadLine_Year.get())-START_YEAR)
        elif int(self.Combo_NewTaskStartTime_Year.get())<int(self.Combo_NewTaskDeadLine_Year.get()):
            return
        
        if int(self.Combo_NewTaskStartTime_Month.get())>int(self.Combo_NewTaskDeadLine_Month.get()):
            self.Combo_NewTaskStartTime_Month.current(int(self.Combo_NewTaskDeadLine_Month.get())-1)
        elif int(self.Combo_NewTaskStartTime_Month.get())<int(self.Combo_NewTaskDeadLine_Month.get()):
            return

        if int(self.Combo_NewTaskStartTime_Day.get())>int(self.Combo_NewTaskDeadLine_Day.get()):
            self.Combo_NewTaskStartTime_Day.current(int(self.Combo_NewTaskDeadLine_Day.get())-1)
        elif int(self.Combo_NewTaskStartTime_Day.get())<int(self.Combo_NewTaskDeadLine_Day.get()):
            return

        if int(self.Combo_NewTaskStartTime_Hour.get())>int(self.Combo_NewTaskDeadLine_Hour.get()):
            self.Combo_NewTaskStartTime_Hour.current(int(self.Combo_NewTaskDeadLine_Hour.get()))
        elif int(self.Combo_NewTaskStartTime_Hour.get())<int(self.Combo_NewTaskDeadLine_Hour.get()):
            return
        
        if int(self.Combo_NewTaskStartTime_Minute.get())>int(self.Combo_NewTaskDeadLine_Minute.get()):
            self.Combo_NewTaskStartTime_Minute.current(int(self.Combo_NewTaskDeadLine_Minute.get()))


# 功能函数
    def Merge_Tasks(self,NewTaskInfoDict:dict,Rows:list):
        """
当新添加的任务有部分重复时，将新任务和已有任务相合并，共同构成一个任务。
        """
        pass


    def NewTask_In_Tasks(self,NewTaskInfoDict:dict)->tuple:
        """
判断新任务是否已经存在于原来的任务列表中。
返回包括2个值：InTaskMode和Rows。
InTaskMode为int，对应不同的情况。
Rows为list，包括了所有有重复的行。
        """
        Rows=[]
        InTaskMode=-1
        NewTaskName=NewTaskInfoDict['任务名']
        NewTaskST=dt.datetime.strptime(NewTaskInfoDict['开始时间'],DATETIME_STR_DEMO)
        NewTaskDL=dt.datetime.strptime(NewTaskInfoDict['截止时间'],DATETIME_STR_DEMO)
        for row in self.TaskDataFrame[self.TaskDataFrame['任务名']==NewTaskName].index:
            TaskST=dt.datetime.strptime(self.TaskDataFrame.loc[row,'开始时间'],DATETIME_STR_DEMO)
            TaskDL=dt.datetime.strptime(self.TaskDataFrame.loc[row,'截止时间'],DATETIME_STR_DEMO)
            
            if NewTaskST>=TaskST and NewTaskDL<=TaskDL:
                InTaskMode=TOTALLY_IN 
                Rows.append(row)
            elif NewTaskST<TaskST and NewTaskDL>TaskDL:
                InTaskMode=TOTALLY_COVER
                Rows.append(row)
            elif (NewTaskST<=TaskST and TaskST<=NewTaskDL<=TaskDL) or(TaskDL>=NewTaskST>=TaskST and NewTaskDL>=TaskDL):
                InTaskMode=PARTLY_IN_SINGLE
                Rows.append(row)

        if len(Rows)==0:
            InTaskMode=TOTALLY_NOT_IN
        elif len(Rows)>1:
            InTaskMode=PARTLY_IN_MULTIPLE
        return InTaskMode,Rows


    def Update_time(self):
        """更新时间"""
        self.NowTime=dt.datetime.now()
        NowTime_Str=self.NowTime.strftime('%Y/%m/%d %H:%M:%S')
        self.Label_NowTime['text']=f'现在系统时间 {NowTime_Str}'
        self.root.after(1000,self.Update_time)#每隔1s更新一下时间


    def Save_file(self):
        """保存文件"""
        if self.change:
            self.TaskDataFrame.to_excel(f"{App_path()}/Tasks.xlsx",sheet_name='Tasks',index=False)
            self.change=False
            print('已保存数据')


    def Auto_save_file(self):
        self.Save_file()
        self.root.after(SAVE_INTERVAL,self.Auto_save_file)#每隔SAVE_INTERVAL保存一下文件


    def Run_app(self):
        """运行程序"""
        self.root.mainloop()


    def Show_data_frame(self):
        print(self.TaskDataFrame)


# 测试功能函数
    def Print_Fine(self,event=None):
        """检测程序是否正常运行"""
        print("Fine")


    def Create_test_task_dataframe(self,num:int):
        """创建测试用的任务数据集"""
        dic={'任务名':[],
            '优先级' :[],
            '开始时间':[],
            '截止时间':[],
            '完成情况':[],
            '备注':[]}
        self.TaskDataFrame=pd.DataFrame(dic)
        DeltaTime=dt.timedelta(hours=1)
        for i in range(num):
            NewTaskInfoDict={
            '任务名':f"Task ({i+1})",
            '优先级' :0,
            '开始时间': dt.datetime.now().strftime(DATETIME_STR_DEMO),
            '截止时间':(dt.datetime.now()+DeltaTime).strftime(DATETIME_STR_DEMO),
            '完成情况':DOING,
            '备注':'测试数据集！！！'}
            self.TaskDataFrame.loc[self.TaskDataFrame.index.size]=NewTaskInfoDict
        
        self.Show_data_frame()



TaskManage=Task_Manage()
TaskManage.App_init()
TaskManage.Assembly_init()
TaskManage.Parameter_correct()
TaskManage.Files_check()
TaskManage.Auto_save_file()#开启自动保存
TaskManage.Create_test_task_dataframe(5)#构建测试数据集


TaskManage.Run_app()