from tkinter import *

root=Tk()
root.geometry('650x500')

canvas=Canvas(root,width=200,height=180,bg='black',scrollregion=(0,0,520,520)) #创建canvas
canvas.place(x = 75, y = 265) #放置canvas的位置
frame=Frame(canvas,bd=1) #把frame放在canvas里
frame.place(x=0,y=0,width=180, height=180) #frame的长宽，和canvas差不多的
vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
vbar.place(x = 180,width=20,height=180)
vbar.configure(command=canvas.yview) 
canvas.config(yscrollcommand=vbar.set) #设置  
canvas.create_window((90,240), window=frame)  #create_window

label1=Label(canvas,text='fijahgfdskhfdsfa')
label1.place(x=0,y=0,height=20,width=30)

root.mainloop()