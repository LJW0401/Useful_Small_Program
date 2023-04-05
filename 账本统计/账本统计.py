import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']  # replace with your installed Chinese font

class Bill_Record:
    def __init__(self) -> None:
        self.Bills=None
        
        
    def Load_Bills_Excel(self,FilePath=''):
        '''Load the Excel file into a Pandas DataFrame'''
        self.Bills=pd.read_excel(FilePath)
        self.Bills.fillna(0, inplace=True)
        
        
    def Show_Monthly_Cost_Type_Pie(self,year=2023,month=1):
        '''Show the percentage of monthly spending by category'''
        start_date = pd.Timestamp(f'{year}-{month}-01')
        end_date = start_date + pd.offsets.MonthEnd(1)
        mask=(self.Bills['日期'] >= start_date) & (self.Bills['日期'] <= end_date)
        SubBills=self.Bills.loc[mask]
        # print(SubBills)
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
        self.Draw_Pie_Chart(datas=Datas,labels=Types,title=f'{year}-{month}消费分类百分比，消费总额:{round(sum(Datas),2)}')
    
    
    def Show_Monthly_Cost_Type_Bar(self,year=2023,month=1):
        # '''Show the percentage of monthly spending by category'''
        start_date = pd.Timestamp(f'{year}-{month}-01')
        end_date = start_date + pd.offsets.MonthEnd(1)
        mask=(self.Bills['日期'] >= start_date) & (self.Bills['日期'] <= end_date)
        SubBills=self.Bills.loc[mask]
        # print(SubBills)
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
        self.Draw_Bar_Chart(y=Datas,x=Types,title=f'{year}-{month}消费分类柱状图，消费总额:{round(sum(Datas),2)}')
    
    
    def Show_Monthly_Payment_Method_Pie(self,year=2023,month=1):
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
        self.Draw_Pie_Chart(datas=Datas,labels=Methods,title=f'{year}-{month}消费支付方式百分比，消费总额:{round(sum(Datas),2)}')
            
    
    
    def Draw_Bar_Chart(self,x,y,xlabel='',ylabel='',title=''):
        '''Draw bar chart'''
        plt.bar(x, y)
        # Add labels and title
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
    
    
    def Draw_Pie_Chart(self,datas,labels,title='',colors=None):
        '''Draw pie chart'''
        fig, ax = plt.subplots(figsize=(9, 9))
        plt.rcParams['font.size'] = 14
        ax.pie(datas, labels=labels, colors=colors, autopct='%1.2f%%')
        ax.legend(labels, loc='best')
        plt.title(title)
        plt.show()

if __name__ =='__main__':
    BillRecord=Bill_Record()
    BillRecord.Load_Bills_Excel('')
    # BillRecord.Show_Monthly_Cost_Type_Bar(month=1)
    BillRecord.Show_Monthly_Payment_Method_Pie(month=3)
