import tkinter as tk


class InfoCheckButton:
    def __init__(self,master,TaskInfo):
        self.cb=tk.Checkbutton(master)
        self.TaskInfo=TaskInfo


    def UpdateInfo(self):
        # 更新文字内容
        self.cb['anchor']='w'
        TaskName=self.TaskInfo['任务名']
        TaskPriority=self.TaskInfo['优先级']
        TaskStartTime=self.TaskInfo['开始时间']
        TaskDeadLine=self.TaskInfo['截止时间']
        TaskNotes=self.TaskInfo['备注']
        self.cb['text']=f'任务名:{TaskName}\n优先级:{TaskPriority}\n开始时间:{TaskStartTime}\n截止时间:{TaskDeadLine}\n备注:{TaskNotes}'
        # 更新状态
        if self.TaskInfo['完成情况']==0:
            self.cb.deselect()
        else:
            self.cb.select()


def func(event):
    print(1)


root = tk.Tk()
root.geometry('650x500')
NewTaskInfoDict={
            '任务名':'任务名',
            '优先级' :0,
            '开始时间':'开始时间',
            '截止时间':'截止时间',
            '完成情况':0,
            '备注':'测试数据集！！！'}
cb1=InfoCheckButton(root,TaskInfo=NewTaskInfoDict)
cb1.UpdateInfo()
cb1.cb.pack()
cb1.cb.bind('<Property>',func)



def print_data():
    print(cb1)


b1 = tk.Button(root,text = "test",command=print_data,height=5, width = 20)
b1.pack()

root.mainloop()