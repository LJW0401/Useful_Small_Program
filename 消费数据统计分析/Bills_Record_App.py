import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import os
import os.path
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import sys

import Bills_Record as BR #用于进行消费分析的库

BRLoaded = BR.Load_Check()
if not BRLoaded:
    print('Error:Bills_Record Class load unsuccessfully!')


CANVAS_WIDTH=900
CANVAS_HEIGHT=450

'''基本操作'''
def App_path():#获得主程序的路径
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


def refine_FileName(Path:str):#返回合适格式的文件路径
    return '/'.join(Path.split('\\'))

def get_file_name(Path:str):#返回文件名
    return Path.split('\\')[-1]

def load_file_path_file(): #加载地址文件
    path=App_path()+'/ConsumptionData.path'
    if not os.path.exists(path):#文件路径不存在
        with open(path,'wb') as f:
            file_path=App_path()+'/BillsRecord.xlsx'
            file_path_coded = file_path.encode('utf-8')
            f.write(file_path_coded)
    with open(path,'rb') as f:
        file_path = f.read()
        file_path = file_path.decode('utf-8')
    if not os.path.exists(file_path):#文件路径不存在
        Empty_DataFrame = pd.DataFrame({'日期':[],'消费额':[],'支付方式':[],'消费类型':[]})
        Empty_DataFrame.to_excel(file_path, sheet_name='Consumptions', index=False)
    print('Files is completed!')
    
    return file_path
    
    
def get_zoom_ratio(OriginalWidth,OriginalHeight):
    yzr=CANVAS_HEIGHT/OriginalHeight
    xzr=CANVAS_WIDTH/OriginalWidth
    return min(xzr,yzr)
'''相关的类'''



'''定义软件的类'''
class Bills_Record:
    def __init__(self) -> None:
        """初始化类"""
        self.version='1.1.1'
        print('App Class init successfully!')
        

#初始化函数
    def App_init(self):
        """程序初始化"""
        self.root=tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.Quit_App)#用于在关闭窗口时退出程序
        self.root.title(f"消费数据分析 v{self.version}")
        self.root.geometry('900x950')
        self.DataFilePath = tk.StringVar(value=load_file_path_file())
        self.Year = tk.StringVar(value='2023')
        self.Month = tk.StringVar(value='1')
        self.Date = tk.StringVar(value='1')
        self.BillsRecord = BR.Bills_Record()
        self.MonthlyConsumptionTypeAnalyseChart = 256 - np.ones((450, 900), dtype=np.uint8)
        self.Year_MonthlyConsumptionChangeAnalyseChart = 256 - np.ones((450, 900), dtype=np.uint8)
        self.BillsRecord.Load_Bills_Excel(FilePath=self.DataFilePath.get())
        print('App init successfully!')


    def Assembly_init(self):
        """
        控件初始化\n
        本软件包含以下几个组成部分（排序不分先后）：\n
            1.按月份对消费的类型，以及消费方式进行分析\n
            2.某年中消费额随月份的变化\n
            3.实现向文件中添加新记录的能力\n
        """
        
        '''
        Frame_Choices
        用于放置可选择选项
        包括：
            年份选择
            月份选择
            保存文件路径选择
        '''
        self.Frame_Choices = tk.Frame(
            self.root,
            # relief='groove',bd=2,height=100,width=100
        )
        self.Frame_Choices.pack(side='top')
        
        '''
        保存的文件路径选择
        '''
        Frame_Choices_File_Path = tk.Frame(
            self.Frame_Choices,
            # relief='groove',bd=2,height=100,width=100
        )
        Frame_Choices_File_Path.pack(side='top')
        
        Label_FilePath = tk.Label(#文件路径提示词
            Frame_Choices_File_Path,
            text='文件路径'
        )
        Label_FilePath.pack(side='left')
        
        self.Entry_FilePath = tk.Entry(#用于输入文件路径
            Frame_Choices_File_Path,
            textvariable=self.DataFilePath,
            width=100
        )
        self.Entry_FilePath.pack(side='left')
        #将self.Entry_FilePath与一个函数绑定，用于在输入文件路径后自动加载数据
        self.Entry_FilePath.bind('<Return>',self.Entry_FilePath_Return_Func)
        
        '''
        日期的选择与确定
        '''
        Frame_Choices_Date = tk.Frame(
            self.Frame_Choices,
            # relief='groove',bd=2,height=100,width=100
        )
        Frame_Choices_Date.pack(side='left')

        Label_DateInput = tk.Label(#年份选择提示词
            Frame_Choices_Date,
            text='输入日期：'
        )
        Label_DateInput.pack(side='left')
        
        self.Entry_YearInput = tk.Entry(#用于输入年份
            Frame_Choices_Date,
            textvariable=self.Year,
            width=6
        )
        self.Entry_YearInput.pack(side='left')
        
        Label_YearChoice = tk.Label(#年份选择提示词
            Frame_Choices_Date,
            text='年'
        )
        Label_YearChoice.pack(side='left')
        
        self.Entry_MonthInput = tk.Entry(#用于输入月份
            Frame_Choices_Date,
            textvariable=self.Month,
            width=6
        )
        self.Entry_MonthInput.pack(side='left')
        
        Label_YearChoice = tk.Label(#月份选择提示词
            Frame_Choices_Date,
            text='月'
        )
        Label_YearChoice.pack(side='left')
        
        self.Entry_DateInput = tk.Entry(#用于输入日期
            Frame_Choices_Date,
            textvariable=self.Date,
            width=6
        )
        # self.Entry_DateInput.pack(side='left')
        
        Label_YearChoice = tk.Label(#日期选择提示词
            Frame_Choices_Date,
            text='日'
        )
        # Label_YearChoice.pack(side='left')
        
        self.Button_StartAnalyse = tk.Button(
            Frame_Choices_Date,
            text='开始分析',
            command=self.Button_StartAnalyse_func
        )
        self.Button_StartAnalyse.pack(side='right',padx=20)
        '''
        计算日均消费
        '''
        Frame_Choices_Date = tk.Frame(
            self.Frame_Choices,
            # relief='groove',bd=2,height=100,width=100
        )
        Frame_Choices_Date.pack(side='right')
        
        self.Label_Daily_Consumption = tk.Label(
            Frame_Choices_Date,
            text='日均消费：--'
        )
        self.Label_Daily_Consumption.pack(side='left')
        
        '''
        Frame_Show
        用于放置显示的图像
        '''
        self.Frame_Show = tk.Frame(
            self.root,
            # relief='groove',bd=2,height=100,width=100
        )
        self.Frame_Show.pack(side='top')
#按月份对消费的类型，以及消费方式进行分析
        '''
        Frame_MonthlyConsumptionTypeAnalyse
        用于放置显示按月计算的消费信息分析
        包含一张消费类型分析的饼图以及一张消费类型分析的柱状图
        '''
        self.Frame_MonthlyConsumptionAnalyse=tk.Frame(
            self.Frame_Show,
            # relief='groove',bd=2,height=100,width=100
        )
        self.Frame_MonthlyConsumptionAnalyse.pack(side='top')
        
        self.Canvas_MonthlyConsumptionTypeAnalyseChart = tk.Canvas(#用来显示每月消费类型的图表
            self.Frame_MonthlyConsumptionAnalyse,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT
        )
        self.Canvas_MonthlyConsumptionTypeAnalyseChart.pack(side='top')
        
        self.Frame_Year_MonthlyConsumptionChangeAnalyse=tk.Frame(
            self.Frame_Show,
            # relief='groove',bd=2,height=100,width=100
        )
        self.Frame_Year_MonthlyConsumptionChangeAnalyse.pack(side='top')
        
        self.Canvas_Year_MonthlyConsumptionChangeAnalyseChart = tk.Canvas(#用来显示每年消费随月份变化的图表
            self.Frame_Year_MonthlyConsumptionChangeAnalyse,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT
        )
        self.Canvas_Year_MonthlyConsumptionChangeAnalyseChart.pack(side='top')
        
        '''
        显示初始空白图像
        '''
        ResizeShape = (CANVAS_WIDTH,CANVAS_HEIGHT)
        img = Image.fromarray(self.MonthlyConsumptionTypeAnalyseChart).resize(ResizeShape)
        self.MonthlyConsumptionTypeAnalyseChart = ImageTk.PhotoImage(img)
        self.Canvas_MonthlyConsumptionTypeAnalyseChart.create_image(0,0,anchor='nw',image=self.MonthlyConsumptionTypeAnalyseChart)
        
        img = Image.fromarray(self.Year_MonthlyConsumptionChangeAnalyseChart).resize(ResizeShape)
        self.Year_MonthlyConsumptionChangeAnalyseChart = ImageTk.PhotoImage(img)
        self.Canvas_Year_MonthlyConsumptionChangeAnalyseChart.create_image(0,0,anchor='nw',image=self.Year_MonthlyConsumptionChangeAnalyseChart)
        
        print('App assembly init successfully!')
#控件函数
    def Blank_Func(self):
        return

    
    def Entry_FilePath_Return_Func(self,event):
        FilePath = self.Entry_FilePath.get()
        print('File path is changed to:',FilePath)
        tk.messagebox.showinfo(title='提示',message='文件路径修改成功！')
        
        return self.BillsRecord.Load_Bills_Excel(FilePath=FilePath)
        
        
    def Button_StartAnalyse_func(self):
        try:
            Year=int(self.Year.get())
            Month = int(self.Month.get())
            MonthlyConsumptionTypeAnalyseChart = np.hstack(
                self.BillsRecord.Monthly_Consumption_Type_Analyse(year=Year,month=Month)
            )
            
            Year_MonthlyConsumptionChangeAnalyseChart = self.BillsRecord.Year_Monthly_Consumption_Change_Analyse(year=Year)
            
            ResizeShape = (CANVAS_WIDTH,CANVAS_HEIGHT)
            img = Image.fromarray(MonthlyConsumptionTypeAnalyseChart).resize(ResizeShape)
            self.MonthlyConsumptionTypeAnalyseChart = ImageTk.PhotoImage(img)
            self.Canvas_MonthlyConsumptionTypeAnalyseChart.create_image(0,0,anchor='nw',image=self.MonthlyConsumptionTypeAnalyseChart)
            
            img = Image.fromarray(Year_MonthlyConsumptionChangeAnalyseChart).resize(ResizeShape)
            self.Year_MonthlyConsumptionChangeAnalyseChart = ImageTk.PhotoImage(img)
            self.Canvas_Year_MonthlyConsumptionChangeAnalyseChart.create_image(0,0,anchor='nw',image=self.Year_MonthlyConsumptionChangeAnalyseChart)

            DailyConsumption = self.BillsRecord.Daily_Consumption(year=Year,month=Month)
            self.Label_Daily_Consumption['text']=f'{Year}年{Month}月日均消费￥{DailyConsumption}'
        except:
            tk.messagebox.showerror(title='错误',message='输入的日期没有对应数据！')
        
        
#功能函数
    def Show_Img(self):
        ResizeShape=(int(self.ImgWidth*self.ZoomRatio),int(self.ImgHeight*self.ZoomRatio))
        img = Image.fromarray(self.GrayImg).resize(ResizeShape)
        self.ShowImg = ImageTk.PhotoImage(img)
        self.Canvas_Image.create_image(0,0,anchor='nw',image=self.ShowImg)


    def Run_app(self):
        """运行程序"""
        self.root.mainloop()
        
    def Quit_App(self):
        sys.exit(0)


'''软件运行'''
BillsRecord=Bills_Record()
BillsRecord.App_init()
BillsRecord.Assembly_init()
BillsRecord.Run_app()
