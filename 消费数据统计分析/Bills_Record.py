import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']  # replace with your installed Chinese font
import numpy as np


def Load_Check():
    print('Bills_Record Class load successfully!')
    return True

        
# 这里的几个分析函数有些问题，会导致在应用以后程序无法关闭


class Bills_Record:
    '''
    用于进行消费分析的集成类，集成了相关的函数以及变量\n
    注：返回的图片都是(np.ndarray类型的RGB图像)
    该类包含以下的分析功能：\n
        Bills_Record.Load_Bills_Excel():从电脑上加载Excel数据集(.xlsx文件)\n
        Bills_Record.Save_Bills_Excel():将内部数据保存为Excel数据集(.xlsx文件)\n
        Bills_Record.Add_New_Record():向表中添加新的消费记录\n
        Bills_Record.Monthly_Consumption_Type_Analyse():分析指定月份的消费额与消费类型的关系，返回一张饼图和柱状图\n
        Bills_Record.Monthly_Consumption_Method_Analyse():分析指定月份的消费额与消费方式的关系，返回一张饼图和柱状图\n
        Bills_Record.Yearly_Consumption_Type_Analyse():分析指定年份的消费额与消费类型的关系，返回一张饼图和柱状图\n
        Bills_Record.Yearly_Consumption_Method_Analyse():分析指定年份的消费额与消费方式的关系，返回一张饼图和柱状图\n
        Bills_Record.Year_Monthly_Consumption_Change_Analyse():分析指定年份中每月消费总额的变化趋势，返回一张折线图\n
    '''
    def __init__(self) -> None:
        self.Bills=None
        self.Chart=None
    
        
    def Check(self):
        print('passed')
    
    
    def Load_Bills_Excel(self,FilePath):
        '''从电脑上加载Excel数据集(.xlsx文件)'''
        self.Bills=pd.read_excel(FilePath)
        self.Bills.fillna(0, inplace=True)
        
    
    def Save_Bills_Excel(self,FilePath):
        '''将内部数据保存为Excel数据集(.xlsx文件)'''
        self.Bills.to_excel(FilePath, sheet_name='Consumptions', index=False)
    
    
    def Add_New_Record(self,DataDict:dict):
        '''向表中添加新的消费记录'''
        self.Bills = self.Bills.append(DataDict, ignore_index=True)
    
    
    def Monthly_Consumption_Type_Analyse(self,year=2023,month=1):
        '''分析指定月份的消费额与消费类型的关系，返回一张饼图和柱状图'''
        start_date = pd.Timestamp(f'{year}-{month}-01')
        end_date = start_date + pd.offsets.MonthEnd(1)
        mask=(self.Bills['日期'] >= start_date) & (self.Bills['日期'] <= end_date)
        SubBills=self.Bills.loc[mask]
        Types=list(SubBills['消费类型'].unique())
        Datas=[]
        for Type in Types[:]:
            mask=self.Bills['消费类型']==Type
            SubSubBills=SubBills.loc[mask]
            Sum=abs(SubSubBills['消费额'].sum())
            if Sum<0.01:
                Types.remove(Type)
            else:
                Datas.append(Sum)
        Types,Datas=zip(*sorted(list(zip(Types,Datas)),reverse=True,key=lambda x:x[1]))
        
        return (
            self.Draw_Pie_Chart(datas=Datas,labels=Types,title=f'{year}-{month}消费分类百分比，消费总额:{round(sum(Datas),2)}'),
            self.Draw_Bar_Chart(y=Datas,x=Types,xlabel='消费类型',ylabel='消费额',title=f'{year}-{month}消费分类柱状图，消费总额:{round(sum(Datas),2)}')
        )
    
    
    def Monthly_Consumption_Method_Analyse(self,year=2023,month=1):
        '''分析指定月份的消费额与消费方式的关系，返回一张饼图和柱状图'''
        start_date = pd.Timestamp(f'{year}-{month}-01')
        end_date = start_date + pd.offsets.MonthEnd(1)
        mask=(self.Bills['日期'] >= start_date) & (self.Bills['日期'] <= end_date)
        SubBills=self.Bills.loc[mask]
        Methods=list(SubBills['支付方式'].unique())
        Datas=[]
        for Method in Methods[:]:
            mask=self.Bills['支付方式']==Method
            SubSubBills=SubBills.loc[mask]
            Sum=abs(SubSubBills['消费额'].sum())
            if Sum<0.01:
                Methods.remove(Method)
            else:
                Datas.append(Sum)
        Methods,Datas=zip(*sorted(list(zip(Methods,Datas)),reverse=True,key=lambda x:x[1]))
        
        return (
            self.Draw_Pie_Chart(datas=Datas,labels=Methods,title=f'{year}-{month}消费支付方式百分比，消费总额:{round(sum(Datas),2)}'),
            self.Draw_Bar_Chart(y=Datas,x=Methods,xlabel='消费支付方式',ylabel='消费额',title=f'{year}-{month}消费支付方式柱状图，消费总额:{round(sum(Datas),2)}')
        )
    
    
    def Yearly_Consumption_Type_Analyse(self,year=2023):
        '''分析指定年份的消费额与消费类型的关系，返回一张饼图和柱状图'''
        start_date = pd.Timestamp(f'{year}-01-01')
        end_date = start_date + pd.offsets.MonthEnd(12)
        mask=(self.Bills['日期'] >= start_date) & (self.Bills['日期'] <= end_date)
        SubBills=self.Bills.loc[mask]
        Types=list(SubBills['消费类型'].unique())
        Datas=[]
        for Type in Types[:]:
            mask=self.Bills['消费类型']==Type
            SubSubBills=SubBills.loc[mask]
            Sum=abs(SubSubBills['消费额'].sum())
            if Sum<0.01:
                Types.remove(Type)
            else:
                Datas.append(Sum)
        Types,Datas=zip(*sorted(list(zip(Types,Datas)),reverse=True,key=lambda x:x[1]))
        
        return (
            self.Draw_Pie_Chart(datas=Datas,labels=Types,title=f'{year}消费分类百分比，消费总额:{round(sum(Datas),2)}'),
            self.Draw_Bar_Chart(y=Datas,x=Types,xlabel='消费类型',ylabel='消费额',title=f'{year}消费分类柱状图，消费总额:{round(sum(Datas),2)}')
        )
    
    
    def Yearly_Consumption_Method_Analyse(self,year=2023):
        '''分析指定年份的消费额与消费方式的关系，返回一张饼图和柱状图'''
        start_date = pd.Timestamp(f'{year}-01-01')
        end_date = start_date + pd.offsets.MonthEnd(12)
        mask=(self.Bills['日期'] >= start_date) & (self.Bills['日期'] <= end_date)
        SubBills=self.Bills.loc[mask]
        Methods=list(SubBills['支付方式'].unique())
        Datas=[]
        for Method in Methods[:]:
            mask=self.Bills['支付方式']==Method
            SubSubBills=SubBills.loc[mask]
            Sum=abs(SubSubBills['消费额'].sum())
            if Sum<0.01:
                Methods.remove(Method)
            else:
                Datas.append(Sum)
        Methods,Datas=zip(*sorted(list(zip(Methods,Datas)),reverse=True,key=lambda x:x[1]))
        
        return (
            self.Draw_Pie_Chart(datas=Datas,labels=Methods,title=f'{year}消费支付方式百分比，消费总额:{round(sum(Datas),2)}'),
            self.Draw_Bar_Chart(y=Datas,x=Methods,xlabel='消费支付方式',ylabel='消费额',title=f'{year}消费支付方式柱状图，消费总额:{round(sum(Datas),2)}')
        )
    
    
    def Year_Monthly_Consumption_Change_Analyse(self,year=2023):
        '''分析指定年份中每月消费总额的变化趋势，返回一张折线图'''
        Datas=[]
        for month in range(1,13):#计算每一个月的消费总额
            start_date = pd.Timestamp(f'{year}-{month}-01')
            end_date = start_date + pd.offsets.MonthEnd(1)
            mask=(self.Bills['日期'] >= start_date) & (self.Bills['日期'] <= end_date)
            Year_Month_ConsumptionDataFrame = self.Bills.loc[mask]
            Sum=abs(Year_Month_ConsumptionDataFrame['消费额'].sum())
            Datas.append(Sum)
        
        return self.Draw_Line_Chart(x=list([str(i)+'月' for i in range(1,13)]),y=Datas,label='消费额',xlabel='月份',ylabel='消费额',title=f'{year}年消费随月份变化曲线')
    
    
#绘制图像的函数
    def Draw_Bar_Chart(self,x,y,xlabel='',ylabel='',title=''):
        '''Draw bar chart'''
        fig, ax = plt.subplots(figsize=(6, 6))
        plt.rcParams['font.size'] = 10
        ax.bar(x, y)
        # Add labels and title
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.title(title)
        for a, b in zip(x, y):#给数据点添加数据
            plt.text(a, b, '%.2f'%b, ha='center', va= 'bottom', fontsize=10)
        
        #Then store the chart as a numpy.ndarray to be a RGB_image
        fig.canvas.draw()
        Image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        Image = Image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        
        if __name__ == '__main__':
            plt.show()
            
        return Image
    
    
    def Draw_Pie_Chart(self,datas,labels,title='',colors=None):
        '''Draw pie chart'''
        fig, ax = plt.subplots(figsize=(6, 6))
        plt.rcParams['font.size'] = 10
        ax.pie(datas, labels=labels, colors=colors, autopct='%1.2f%%')
        ax.legend(labels, loc='upper right')
        plt.title(title)
        
        #Then store the chart as a numpy.ndarray to be a RGB_image
        fig.canvas.draw()
        Image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        Image = Image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        
        if __name__ == '__main__':
            plt.show()
            
        return Image


    def Draw_Line_Chart(self,x,y,label='',xlabel='',ylabel='',title='',figsize=(12, 6)):
        '''Draw line chart'''
        fig, ax = plt.subplots(figsize=figsize)
        plt.rcParams['font.size'] = 10
        ax.plot(x, y, ls='--', lw=1.0, c='Red', marker='.', label=label)
        ax.legend(loc='upper right')
        plt.grid(True)
        # Add labels and title
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.title(title)
        for a, b in zip(x, y):#给数据点添加数据
            plt.text(a, b, '%.2f'%b, ha='center', va= 'bottom', fontsize=10)

        #Then store the chart as a numpy.ndarray to be a RGB_image
        fig.canvas.draw()
        Image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        Image = Image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        
        if __name__ == '__main__':
            plt.show()
            
        return Image
    
    
if __name__ == '__main__':
    BillsRecord=Bills_Record()
    BillsRecord.Load_Bills_Excel('E:\#LJW\#Python_APPs\Bills_Record/BillsRecord.xlsx')
    # print(BillsRecord.Bills)
    # BillsRecord.Add_New_Record({'日期':pd.Timestamp('2025-01-01'),'消费额':-1000,'支付方式':'微信钱包','消费类型':'测试'})
    # print(BillsRecord.Bills)
    
    BillsRecord.Monthly_Consumption_Type_Analyse(month=4)
    # BillsRecord.Yearly_Consumption_Type_Analyse(year=2023)
    # BillsRecord.Yearly_Consumption_Method_Analyse(year=2023)

    BillsRecord.Year_Monthly_Consumption_Change_Analyse(year=2023)
