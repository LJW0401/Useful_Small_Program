import tkinter as tk

class Checkbutton(tk.Checkbutton):
    def __init__(self, container,TaskInfo, *args, **kwargs):
        super().__init__(container,*args, **kwargs)
        self.TaskInfo=TaskInfo

root = tk.Tk()
root.geometry('650x500')
cb1=Checkbutton(root,TaskInfo={'a':111,'b':222},text='1234567')
cb1.pack()

root.mainloop()