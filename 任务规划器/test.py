import tkinter as tk

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
    
    def place_info(self):
        return self.canvas.place_info()




root=tk.Tk()
root.geometry('650x500')

# canvas=Canvas(root,width=200,height=180,bg='black') #创建canvas
# scrollbar=Scrollbar(canvas,orient=VERTICAL,command=canvas.yview) #竖直滚动条
# frame=Frame(canvas) #把frame放在canvas里
# frame.place(x=0,y=0,width=180, height=180) #frame的长宽，和canvas差不多的
# frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# canvas.create_window((0,0), window=frame)  #create_window
# canvas.configure(yscrollcommand=scrollbar.set) #设置  
# canvas.place(x = 0, y = 0) #放置canvas的位置
# scrollbar.place(x = 182,y=2,width=20,height=180)
# # scrollbar.pack(side="right", fill="y")
# def _on_mousewheel(event):  # 鼠标滚轮
#     canvas.yview_scroll(int(-1*(event.delta/120)), "units")
# canvas.bind("<MouseWheel>", _on_mousewheel)  # 绑定鼠标滚轮
# frame.bind("<MouseWheel>", _on_mousewheel)  # 绑定鼠标滚轮
# # vbar.configure(command=canvas.yview) 

frame=ScrollbarFrame(root,200,200)
frame.place(x=60,y=10)


labels=[]
for i in range(10):
    label=tk.Label(frame.frame,text=f'{i}'*8)
    labels.append(label)
    labels[i].bind("<MouseWheel>", frame.on_mousewheel)
    labels[i].pack()
button=tk.Button(frame.frame,text='fijahgfdskhfdsfa')
button.pack()
button.destroy()
for i in range(5):
    labels[i].destroy()
print(len(labels))
root.mainloop()