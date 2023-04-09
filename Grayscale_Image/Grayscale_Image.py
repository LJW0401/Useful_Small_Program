import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import os
import os.path
import cv2
import numpy as np
from PIL import Image, ImageTk

CANVAS_WIDTH=800
CANVAS_HEIGHT=800
'''基本操作'''
def App_path():#获得主程序的路径
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


def refine_FileName(Path:str):#返回合适格式的文件路径
    return '/'.join(Path.split('\\'))

def get_file_name(Path:str):#返回文件名
    return Path.split('\\')[-1]

'''相关函数'''
#加载图像
def load_picture(path):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    return img


#获取阈值
def get_thresh(img):
    return round(img.mean())


#处理图像
def deal_img(img,mid=128):
    # Apply adaptive thresholding
    threshed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img_filtered=threshed.copy()

    for _ in range(10):
        # Apply median filter to remove salt-and-pepper noise
        img_filtered = cv2.medianBlur(img_filtered, 3)
        # Apply bilateral filter to preserve edges and details
        img_filtered = cv2.bilateralFilter(img_filtered, 7, 75, 75)
    # cv2.imshow('Thresholded Image', cv2.resize(np.hstack((threshed,img_filtered)),(0,0),fx=0.25,fy=0.25))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img_filtered


'''相关的类'''



'''定义软件的类'''
class Grayfy_Image:
    def __init__(self) -> None:
        """初始化类"""
        self.version='2.0.0'
        self.OriImg=None
        self.GrayImg=None
        self.Thresh=128
        self.ShowImg=None
        self.ZoomRatio=1
        self.ImgWidth=0
        self.ImgHeight=0
        
    

#初始化函数
    def App_init(self):
        """程序初始化"""
        self.root=tk.Tk()
        self.root.title(f"图像黑白化 v{self.version}")
        self.root.geometry('800x900')
        # mkdir(App_path()+'/img')


    def Assembly_init(self):
        """控件初始化"""
    #显示图像的部分
        Frame_ShowImage=tk.Frame(
            self.root,
            # relief='groove',bd=1
            )
        Frame_ShowImage.pack(side='top')

        
        self.Canvas_Image=tk.Canvas(
            Frame_ShowImage,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT
        )
        self.Canvas_Image.pack(side='top')

    #操作按键区域
        Frame_Handle=tk.Frame(
            self.root,
            # relief='groove',bd=1
            )
        Frame_Handle.pack(side='top',fill='x')

        #图片地址区域
        Frame_ImagePath=tk.Frame(
            Frame_Handle,
            # relief='groove',bd=1
            )
        Frame_ImagePath.pack(side='top',fill='x')

        tk.Label(
            Frame_ImagePath,
            text='原始图片路径',
            font=('黑体',15)
            ).pack(side='left')
        
        self.ImagePath=tk.StringVar(value='E:\homework_img_deal\original\w1-1.jpg')
        self.Entry_ImagePath=tk.Entry(
            Frame_ImagePath,
            textvariable=self.ImagePath,
            font=('黑体',15)
            )
        self.Entry_ImagePath.pack(side='left',fill='x',expand=True)



        #图像黑白化的按钮
        Frame_Button_Handling=tk.Frame(
            Frame_Handle,
            # relief='groove',bd=1
        )
        Frame_Button_Handling.pack(side='top',fill='x')
        Button_Handling=tk.Button(
            Frame_Button_Handling,
            text='黑白化图片',
            font=('黑体',15),
            command=self.Button_Handling_Func
        )
        Button_Handling.pack(side='left',pady=5,padx=5)

        #保存图像
        self.Button_Save_Image=tk.Button(
            Frame_Button_Handling,
            text='保存图像',
            font=('黑体',15),
            command=self.Button_Save_Image_Func
        )
        self.Button_Save_Image.pack(side='right',padx=5)

        #黑白化时的阈值
        Frame_Mid_Thresh=tk.Frame(
            Frame_Button_Handling,
            # relief='groove',bd=1
        )
        # Frame_Mid_Thresh.pack(side='left',fill='x',padx=100)

        
        self.Button_Mid_Thresh_DD=tk.Button(
            Frame_Mid_Thresh,
            text='<<',
            command=self.Button_Mid_Thresh_DD_Func
        )
        self.Button_Mid_Thresh_DD.pack(side='left',padx=5)
        self.Button_Mid_Thresh_Done=tk.Button(
            Frame_Mid_Thresh,
            text='<',
            command=self.Button_Mid_Thresh_Done_Func
        )
        self.Button_Mid_Thresh_Done.pack(side='left',padx=5)
        self.Label_Mid_Thresh=tk.Label(
            Frame_Mid_Thresh,
            text='---',
            font=('黑体',15),
            width=4
        )
        self.Label_Mid_Thresh.pack(side='left',padx=5)
        self.Button_Mid_Thresh_Up=tk.Button(
            Frame_Mid_Thresh,
            text='>',
            command=self.Button_Mid_Thresh_Up_Func
        )
        self.Button_Mid_Thresh_Up.pack(side='left',padx=5)
        self.Button_Mid_Thresh_UU=tk.Button(
            Frame_Mid_Thresh,
            text='>>',
            command=self.Button_Mid_Thresh_UU_Func
        )
        self.Button_Mid_Thresh_UU.pack(side='left',padx=5)
        # tk.Label(Frame_Mid_Thresh,width=30).pack(side='right')
        # Scroll_Mid_Thresh=tk.Scrollbar(
        #     Frame_Mid_Thresh,
        #     orient='horizontal'
        # )
        # Scroll_Mid_Thresh.pack(side='left',padx=5,fill='x',expand=True)
        
#控件函数
    def Blank_Func(self):
        return

    def Button_Handling_Func(self):
        self.OriImg = load_picture(self.ImagePath.get())
        print('Load Sussessfully')
        self.Thresh = 120 #get_thresh(self.OriImg)
        self.Grayfy_Image()
        
        self.Label_Mid_Thresh['text']=str(self.Thresh)

        self.ImgWidth=self.OriImg.shape[1]
        self.ImgHeight=self.OriImg.shape[0]
        yzr=CANVAS_HEIGHT/self.ImgHeight
        xzr=CANVAS_WIDTH/self.ImgWidth
        self.ZoomRatio=min(xzr,yzr)

        self.Show_Img()
        
    

    def Button_Mid_Thresh_Done_Func(self):
        self.Thresh-=1
        if self.Thresh<0:
            self.Thresh=0
        self.Grayfy_Image()
        self.Show_Img()
        self.Label_Mid_Thresh['text']=str(self.Thresh)


    def Button_Mid_Thresh_DD_Func(self):
        self.Thresh-=10
        if self.Thresh<0:
            self.Thresh=0
        self.Grayfy_Image()
        self.Show_Img()
        self.Label_Mid_Thresh['text']=str(self.Thresh)


    def Button_Mid_Thresh_Up_Func(self):
        self.Thresh+=1
        if self.Thresh>255:
            self.Thresh=255
        self.Grayfy_Image()
        self.Show_Img()
        self.Label_Mid_Thresh['text']=str(self.Thresh)

    
    def Button_Mid_Thresh_UU_Func(self):
        self.Thresh+=10
        if self.Thresh>255:
            self.Thresh=255
        self.Grayfy_Image()
        self.Show_Img()
        self.Label_Mid_Thresh['text']=str(self.Thresh)


    def Button_Save_Image_Func(self):
        path_=App_path()+'/'+get_file_name(self.ImagePath.get())
        cv2.imwrite(path_,self.GrayImg)#保存图像
        
#功能函数
    def Grayfy_Image(self):#灰度化图像
        # Img_Done=deal_img(self.OriImg,self.Thresh)
        # path_=App_path()+'/'+get_file_name(self.ImagePath.get())
        # cv2.imwrite(path_,Img_Done)#保存图像
        self.GrayImg=deal_img(self.OriImg,self.Thresh)
        


    def Show_Img(self):
        ResizeShape=(int(self.ImgWidth*self.ZoomRatio),int(self.ImgHeight*self.ZoomRatio))
        # img = Image.open(App_path()+'/'+get_file_name(self.ImagePath.get())).resize(ResizeShape)
        # self.ShowImg = ImageTk.PhotoImage(img)
        img = Image.fromarray(self.GrayImg).resize(ResizeShape)
        # img.show()
        self.ShowImg = ImageTk.PhotoImage(img)
        # self.ShowImg.resize(ResizeShape)
        self.Canvas_Image.create_image(0,0,anchor='nw',image=self.ShowImg )

        # cv2.imshow('Thresholded Image', cv2.resize(self.GrayImg,(0,0),fx=0.25,fy=0.25))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def Run_app(self):
        """运行程序"""
        self.root.mainloop()


'''软件运行'''
GrayfyImage=Grayfy_Image()
GrayfyImage.App_init()
GrayfyImage.Assembly_init()

GrayfyImage.Run_app()
