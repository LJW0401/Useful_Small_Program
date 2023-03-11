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
'''basic operation'''
def App_path():#get the path of the main program
    import sys
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


def mkdir(path):#build the folder path
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)


def refine_FileName(Path:str):#return proper file path
    return '/'.join(Path.split('\\'))

def get_file_name(Path:str):#return file name
    return Path.split('\\')[-1]

'''relevant function'''
#load image
def load_picture(path):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    return img


#get thresh
def get_thresh(img):
    return round(img.mean())


#deal image
def deal_img(img,mid=128):
    ret,dst=cv2.threshold(img,mid,255,cv2.THRESH_BINARY)
    return dst


'''relevant class'''

class Grayfy_Image:
    def __init__(self) -> None:
        """init"""
        self.version='1.0.0'
        self.OriImg=None
        self.Thresh=128
        self.ShowImg=None
        self.ZoomRatio=1
        self.ImgWidth=0
        self.ImgHeight=0
    

#init function
    def App_init(self):
        """init app"""
        self.root=tk.Tk()
        self.root.title(f"图像黑白化 v{self.version}")
        self.root.geometry('800x900')
        # mkdir(App_path()+'/img')


    def Assembly_init(self):
        """init assembly"""
    #the part to show image
        Frame_ShowImage=tk.Frame(
            self.root,
            )
        Frame_ShowImage.pack(side='top')

        
        self.Canvas_Image=tk.Canvas(
            Frame_ShowImage,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT
        )
        self.Canvas_Image.pack(side='top')

    #the part to handle
        Frame_Handle=tk.Frame(
            self.root,
            )
        Frame_Handle.pack(side='top',fill='x')

        #the image path
        Frame_ImagePath=tk.Frame(
            Frame_Handle,
            )
        Frame_ImagePath.pack(side='top',fill='x')

        tk.Label(
            Frame_ImagePath,
            text='原始图片路径',
            font=('黑体',15)
            ).pack(side='left')
        
        self.ImagePath=tk.StringVar(value='---init path---')
        self.Entry_ImagePath=tk.Entry(
            Frame_ImagePath,
            textvariable=self.ImagePath,
            font=('黑体',15)
            )
        self.Entry_ImagePath.pack(side='left',fill='x',expand=True)



        #Grayscale_Image button
        Frame_Button_Handling=tk.Frame(
            Frame_Handle,
        )
        Frame_Button_Handling.pack(side='top',fill='x')
        Button_Handling=tk.Button(
            Frame_Button_Handling,
            text='黑白化图片',
            font=('黑体',15),
            command=self.Button_Handling_Func
        )
        Button_Handling.pack(side='left',pady=5,padx=5)

        #show thresh
        Frame_Mid_Thresh=tk.Frame(
            Frame_Button_Handling,
        )
        Frame_Mid_Thresh.pack(side='left',fill='x',padx=100)

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

        
#functions for assemblies
    def Blank_Func(self):
        return

    def Button_Handling_Func(self):
        self.OriImg = load_picture(self.ImagePath.get())
        print('Load Sussessfully')
        self.Thresh = get_thresh(self.OriImg)
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


#function
    def Grayfy_Image(self):   #grayscale image
        Img_Done=deal_img(self.OriImg,self.Thresh)
        path_=App_path()+'/'+get_file_name(self.ImagePath.get())
        cv2.imwrite(path_,Img_Done)  #save image


    def Show_Img(self):
        ResizeShape=(int(self.ImgWidth*self.ZoomRatio),int(self.ImgHeight*self.ZoomRatio))
        img = Image.open(App_path()+'/'+get_file_name(self.ImagePath.get())).resize(ResizeShape)
        self.ShowImg = ImageTk.PhotoImage(img)
        self.Canvas_Image.create_image(0,0,anchor='nw',image=self.ShowImg )


    def Run_app(self):
        """run"""
        self.root.mainloop()


'''run'''
GrayfyImage=Grayfy_Image()
GrayfyImage.App_init()
GrayfyImage.Assembly_init()

GrayfyImage.Run_app()
