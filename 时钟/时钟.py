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


class Clock:
    def __init__(self) -> None:
        """播放器初始化"""
        '''变量'''
        self.playing=False
        self.networking=False
        self.mp3Files=[]
        '''初始化'''
        self.version='1.0.0'
        self.root=tk.Tk()
        self.root.title(f'时钟 v{self.version}')
        self.root.geometry('400x400')
        self.AssemblyInit()#加载控件
    

    def blank_func(self):
        """空函数，未开发完的按钮等控件使用"""
        pass


    def run_app(self):
        """运行程序"""
        self.root.mainloop()


    def AssemblyInit(self):
        """控件初始化"""
        '''Frame'''
        self.ButtonsFrame=tk.Frame(self.root,relief='groove',bd=2)

        '''标签'''
        self.label1=tk.Label(self.root,text='123',font=('黑体',15),anchor="w")
        
        '''按钮'''
        self.net=tk.Button(self.root,text='音乐来源：本地',font=('黑体',15),command=self.network)
        self.SP=tk.Button(self.ButtonsFrame,text='播放',font=('黑体',15),command=self.play_stop)
        self.Last=tk.Button(self.ButtonsFrame,text='上一首',font=('黑体',15),command=self.blank_func)
        self.Next=tk.Button(self.ButtonsFrame,text='下一首',font=('黑体',15),command=self.blank_func)
        '''滚动条'''
        # self.play = tk.Scrollbar(self.root)
        # scroll_1.place(x=260,y=70,height=270,width=20)
        '''布局'''
            #Frame
        self.ButtonsFrame.place(x=20,y=70,width=235,height=50)
            #标签
        self.label1.place(x=0,y=0)
            #按钮
        self.net.place(x=10,y=7,width=170,height=30)#音乐来源
        self.Last.place(x=10,y=7,width=70,height=30)#上一首
        self.SP.place(x=80,y=7,width=70,height=30)#播放/暂停
        self.Next.place(x=150,y=7,width=70,height=30)#下一首


clock=Clock()
clock.run_app()