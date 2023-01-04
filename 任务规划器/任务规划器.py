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



'''定义显示区域的物件的类'''
class Task_CheckButton:
    def __init__(self,TaskInfo,master) -> None:
        self.TaskInfo=TaskInfo
        self.CheckButton=tk.Checkbutton(master,anchor='w')
    

    def Update(self):
        """更新复选框内的内容"""
        pass


'''定义软件的类'''
class Task_Manage:
    def __init__(self) -> None:
        """初始化类"""
        self.version='1.0.0'
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
# root部分
        '''Frame'''
        self.Frame_AddTask=tk.LabelFrame(self.root,text='添加新任务')
        self.Frame_NowTask=tk.LabelFrame(self.root,text='当前任务')
        # 试试用canvas来控制滚动
        self.Canvas_Tasks_Show_Range=tk.Canvas(self.Frame_NowTask,bg='black',scrollregion=(0,0,0,520))
        # self.Frame_Tasks_Show_Range=tk.Frame(self.Frame_NowTask,relief='groove',bd=1)   #此处先用'groove'下凹来增强显示效果，功能开发完成后换成'flat'与平面保持平行，增加美观。
        self.Frame_Tasks_Show=tk.Frame(self.Canvas_Tasks_Show_Range,relief='groove',bd=1)#此处先用'groove'下凹来增强显示效果，功能开发完成后换成'flat'与平面保持平行，增加美观。
        self.NowTask_yScroll = tk.Scrollbar(self.root)
        # 关联显示区域和滚动条
        self.NowTask_yScroll.config(command=self.Canvas_Tasks_Show_Range.yview)
        self.Canvas_Tasks_Show_Range.config(yscrollcommand=self.NowTask_yScroll.set)
        '''Label'''
        self.Label_NowTime=tk.Label(
                        self.root,
                        text='现在系统时间 ----/--/-- --:--:--',
                        font=('黑体',15),
                        anchor='w')
        Label_ChooseDate=tk.Label(self.root,text='选择日期：',anchor="w")
        '''ComboBox'''
        #选择年份
        self.Combo_ChooseDate_Year=tkinter.ttk.Combobox(
                self.root,values=[i for i in range(START_YEAR,FINISH_YEAR+1)])
        self.Combo_ChooseDate_Year.current(0)

        self.Combo_ChooseDate_Month=tkinter.ttk.Combobox(
                self.root,values=[i for i in range(1,13)])
        self.Combo_ChooseDate_Month.current(0)

        self.Combo_ChooseDate_Day=tkinter.ttk.Combobox(
                self.root,values=[i for i in range(1,32)])
        self.Combo_ChooseDate_Day.current(0)
        self.Combo_ChooseDate_Month.bind('<<ComboboxSelected>>',self.Fix_number_of_day_ChooseDate)
        '''布局'''
        DpiX=5;LabelWidth=60;LabelHeight=20;DeltaDpi=5
        # 显示系统时间
        self.Label_NowTime.place(x=10,y=10,height=20,width=400)
        # 选择具体时间
        Label_ChooseDate.place(x=10,y=35,height=20,width=60)
        self.Combo_ChooseDate_Year.place(
                x=int(Label_ChooseDate.place_info()['x'])+int(Label_ChooseDate.place_info()['width'])+DeltaDpi,
                y=int(Label_ChooseDate.place_info()['y'])+2,
                height=20,width=50)
        self.Combo_ChooseDate_Month.place(
                x=int(self.Combo_ChooseDate_Year.place_info()['x'])+int(self.Combo_ChooseDate_Year.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_ChooseDate_Year.place_info()['y']),
                height=20,width=40)
        self.Combo_ChooseDate_Day.place(
                x=int(self.Combo_ChooseDate_Month.place_info()['x'])+int(self.Combo_ChooseDate_Month.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_ChooseDate_Month.place_info()['y']),
                height=20,width=40)
        # 显示任务
        self.Frame_NowTask.place(x=10,y=60,height=180,width=310)

#--------------------------------------------------------------------------------
        self.Canvas_Tasks_Show_Range.place(x=0,y=0,height=150,width=150)#参数还需调整
        self.Frame_Tasks_Show.place(x=10,y=10,height=30,width=30)      #参数还需调整
#================================================================================

        self.NowTask_yScroll.place(
                x=int(self.Frame_NowTask.place_info()['x'])+int(self.Frame_NowTask.place_info()['width']),
                y=60,
                height=self.Frame_NowTask.place_info()['height'],
                width=20)
        #添加任务
        self.Frame_AddTask.place(x=10,y=250,height=200,width=310)
# 显示当前应做的任务
# 添加新任务的模块
        '''Label'''
        Label_NewTaskName=tk.Label(self.Frame_AddTask,text='任务名：',anchor="w")
        Label_NewTaskStartTime=tk.Label(self.Frame_AddTask,text='开始时间：',anchor='w')
        Label_NewTaskDeadLine=tk.Label(self.Frame_AddTask,text='截止时间：',anchor='w')
        Label_NewTaskPriority=tk.Label(self.Frame_AddTask,text='优先级：',anchor='w')
        Label_NewTaskNotes=tk.Label(self.Frame_AddTask,text='任务备注：',anchor='w')
        Label_NewTaskRepetitionFrequency=tk.Label(self.Frame_AddTask,text='重复频率：',anchor='w')
        Label_NewTaskRepetitionTimes=tk.Label(self.Frame_AddTask,text='重复次数：',anchor='w')
        '''Button'''
        self.Button_AddNewTask=tk.Button(self.Frame_AddTask,text='添加新任务',command=self.Button_Add_new_task)
        '''Entry'''
        #新任务名
        self.Entry_NewTaskName=tk.Entry(self.Frame_AddTask)
        #重复次数
        self.Entry_NewTaskRepetitionTimes=tk.Entry(self.Frame_AddTask)
        '''Text'''
        self.Txt_NewTaskNotes = tk.Text(self.Frame_AddTask)#,font=('黑体',15))
        self.Txt_NewTaskNotes_yScroll = tk.Scrollbar(self.Frame_AddTask)
        # 两个控件关联
        self.Txt_NewTaskNotes_yScroll.config(command=self.Txt_NewTaskNotes.yview)
        self.Txt_NewTaskNotes.config(yscrollcommand=self.Txt_NewTaskNotes_yScroll.set)
        '''ComboBox'''
        #开始日期的年份
        self.Combo_NewTaskStartTime_Year=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(START_YEAR,FINISH_YEAR+1)])
        self.Combo_NewTaskStartTime_Year.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)
        self.Combo_NewTaskStartTime_Year.current(0)
        #开始日期的月份、日期
        self.Combo_NewTaskStartTime_Month=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(1,13)])
        self.Combo_NewTaskStartTime_Month.current(0)
        self.Combo_NewTaskStartTime_Day=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(1,32)])
        self.Combo_NewTaskStartTime_Day.current(0)
        self.Combo_NewTaskStartTime_Day.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)
        self.Combo_NewTaskStartTime_Month.bind('<<ComboboxSelected>>',self.Fix_number_of_day_StartTime)
        #开始日期的小时
        self.Combo_NewTaskStartTime_Hour=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(0,24)])
        self.Combo_NewTaskStartTime_Hour.current(0)
        self.Combo_NewTaskStartTime_Hour.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)
        #开始日期的分钟
        self.Combo_NewTaskStartTime_Minute=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(0,60)])
        self.Combo_NewTaskStartTime_Minute.current(0)
        self.Combo_NewTaskStartTime_Minute.bind('<<ComboboxSelected>>',self.Click_StartTime_ensure_DeadLine)

        #截止日期的年份
        self.Combo_NewTaskDeadLine_Year=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(START_YEAR,FINISH_YEAR+1)])
        self.Combo_NewTaskDeadLine_Year.current(0)
        self.Combo_NewTaskDeadLine_Year.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        #截止日期的月份、日期
        self.Combo_NewTaskDeadLine_Month=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(1,13)])
        self.Combo_NewTaskDeadLine_Month.current(0)
        self.Combo_NewTaskDeadLine_Day=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(1,32)])
        self.Combo_NewTaskDeadLine_Day.current(0)
        self.Combo_NewTaskDeadLine_Day.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        self.Combo_NewTaskDeadLine_Month.bind('<<ComboboxSelected>>',self.Fix_number_of_day_DeadLine)
        #截止日期的小时
        self.Combo_NewTaskDeadLine_Hour=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(0,24)])
        self.Combo_NewTaskDeadLine_Hour.current(0)
        self.Combo_NewTaskDeadLine_Hour.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        #截止日期的分钟
        self.Combo_NewTaskDeadLine_Minute=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(0,60)])
        self.Combo_NewTaskDeadLine_Minute.current(0)
        self.Combo_NewTaskDeadLine_Minute.bind('<<ComboboxSelected>>',self.Click_DeadLine_ensure_StartTime)
        #优先级
        self.Combo_NewTaskPriority=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=[i for i in range(0,5)])
        self.Combo_NewTaskPriority.current(0)
        #重复频率
        self.Combo_NewTaskRepetitionFrequency=tkinter.ttk.Combobox(
                self.Frame_AddTask,values=REPETITION_FREQUENCY_LIST[:3])
        self.Combo_NewTaskRepetitionFrequency.current(0)
        '''布局'''
        DpiX=5;LabelWidth=60;LabelHeight=20;DeltaDpi=5
        ## 添加任务名
        Label_NewTaskName.place(x=5,y=0,height=LabelHeight,width=LabelWidth)
        self.Entry_NewTaskName.place(
                x=DpiX+LabelWidth,
                y=int(Label_NewTaskName.place_info()['y'])+2,
                height=18,width=230)
        ## 添加开始时间
        Label_NewTaskStartTime.place(
                x=DpiX,
                y=int(Label_NewTaskName.place_info()['y'])+LabelHeight+DeltaDpi,
                height=LabelHeight,width=LabelWidth)
        self.Combo_NewTaskStartTime_Year.place(
                x=DpiX+LabelWidth,
                y=int(Label_NewTaskStartTime.place_info()['y'])+2,
                height=20,width=50)
        self.Combo_NewTaskStartTime_Month.place(
                x=int(self.Combo_NewTaskStartTime_Year.place_info()['x'])+int(self.Combo_NewTaskStartTime_Year.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskStartTime_Year.place_info()['y']),
                height=20,width=40)
        self.Combo_NewTaskStartTime_Day.place(
                x=int(self.Combo_NewTaskStartTime_Month.place_info()['x'])+int(self.Combo_NewTaskStartTime_Month.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskStartTime_Month.place_info()['y']),
                height=20,width=40)
        self.Combo_NewTaskStartTime_Hour.place(
                x=int(self.Combo_NewTaskStartTime_Day.place_info()['x'])+int(self.Combo_NewTaskStartTime_Day.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskStartTime_Day.place_info()['y']),
                height=20,width=40)
        self.Combo_NewTaskStartTime_Minute.place(
                x=int(self.Combo_NewTaskStartTime_Hour.place_info()['x'])+int(self.Combo_NewTaskStartTime_Hour.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskStartTime_Hour.place_info()['y']),
                height=20,width=40)
        ## 添加截止时间
        Label_NewTaskDeadLine.place(
                x=DpiX,
                y=int(Label_NewTaskStartTime.place_info()['y'])+LabelHeight+DeltaDpi,
                height=LabelHeight,width=LabelWidth)
        self.Combo_NewTaskDeadLine_Year.place(
                x=int(Label_NewTaskDeadLine.place_info()['x'])+int(Label_NewTaskDeadLine.place_info()['width']),
                y=int(Label_NewTaskDeadLine.place_info()['y'])+2,
                height=20,width=50)
        self.Combo_NewTaskDeadLine_Month.place(
                x=int(self.Combo_NewTaskDeadLine_Year.place_info()['x'])+int(self.Combo_NewTaskDeadLine_Year.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskDeadLine_Year.place_info()['y']),
                height=20,width=40)
        self.Combo_NewTaskDeadLine_Day.place(
                x=int(self.Combo_NewTaskDeadLine_Month.place_info()['x'])+int(self.Combo_NewTaskDeadLine_Month.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskDeadLine_Month.place_info()['y']),
                height=20,width=40)
        self.Combo_NewTaskDeadLine_Hour.place(
                x=int(self.Combo_NewTaskDeadLine_Day.place_info()['x'])+int(self.Combo_NewTaskDeadLine_Day.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskDeadLine_Day.place_info()['y']),
                height=20,width=40)
        self.Combo_NewTaskDeadLine_Minute.place(
                x=int(self.Combo_NewTaskDeadLine_Hour.place_info()['x'])+int(self.Combo_NewTaskDeadLine_Hour.place_info()['width'])+DeltaDpi,
                y=int(self.Combo_NewTaskDeadLine_Hour.place_info()['y']),
                height=20,width=40)
        ## 添加备注
        Label_NewTaskNotes.place(
                x=DpiX,
                y=int(Label_NewTaskDeadLine.place_info()['y'])+LabelHeight+DeltaDpi,
                height=LabelHeight,width=LabelWidth)
        self.Txt_NewTaskNotes.place(
                x=int(Label_NewTaskNotes.place_info()['x'])+int(Label_NewTaskNotes.place_info()['width']),
                y=int(Label_NewTaskNotes.place_info()['y'])+2,
                height=35,width=210)
        self.Txt_NewTaskNotes_yScroll.place(
                x=int(self.Txt_NewTaskNotes.place_info()['x'])+int(self.Txt_NewTaskNotes.place_info()['width']),
                y=int(self.Txt_NewTaskNotes.place_info()['y']),
                height=int(self.Txt_NewTaskNotes.place_info()['height']),width=20)
        ## 选择重复频率。次数
        Label_NewTaskRepetitionFrequency.place(
                x=DpiX,
                y=int(Label_NewTaskNotes.place_info()['y'])+LabelHeight+DeltaDpi*4,
                height=LabelHeight,width=LabelWidth)
        self.Combo_NewTaskRepetitionFrequency.place(
                x=int(Label_NewTaskRepetitionFrequency.place_info()['x'])+int(Label_NewTaskRepetitionFrequency.place_info()['width'])+2,
                y=int(Label_NewTaskRepetitionFrequency.place_info()['y']),
                height=20,width=60)
        Label_NewTaskRepetitionTimes.place(
                x=int(Label_NewTaskRepetitionFrequency.place_info()['x'])+int(Label_NewTaskRepetitionFrequency.place_info()['width'])+int(self.Combo_NewTaskRepetitionFrequency.place_info()['width'])+DeltaDpi*3,
                y=int(Label_NewTaskRepetitionFrequency.place_info()['y']),
                height=LabelHeight,width=LabelWidth)
        self.Entry_NewTaskRepetitionTimes.place(
                x=int(Label_NewTaskRepetitionTimes.place_info()['x'])+int(Label_NewTaskRepetitionTimes.place_info()['width'])+DeltaDpi,
                y=int(Label_NewTaskRepetitionTimes.place_info()['y'])+2,
                height=18,width=90)
        ## 添加优先级
        Label_NewTaskPriority.place(
                x=DpiX,
                y=int(Label_NewTaskRepetitionFrequency.place_info()['y'])+LabelHeight+DeltaDpi*3,
                height=LabelHeight,width=LabelWidth)
        self.Combo_NewTaskPriority.place(
                x=int(Label_NewTaskPriority.place_info()['x'])+int(Label_NewTaskPriority.place_info()['width'])+DeltaDpi,
                y=int(Label_NewTaskPriority.place_info()['y'])+2,
                height=20,width=40)
        ## 添加新任务按钮
        self.Button_AddNewTask.place(
                x=int(self.Combo_NewTaskPriority.place_info()['x'])+int(self.Combo_NewTaskPriority.place_info()['width'])+DeltaDpi*21,
                y=int(Label_NewTaskPriority.place_info()['y'])-5,
                height=30,width=80)
        

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