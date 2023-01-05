from tkinter import * 

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self,bg='black')
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        def _on_mousewheel(event):  # 鼠标滚轮
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)  # 绑定鼠标滚轮


root = Tk()
# root.geometry('650x500')

frame = ScrollableFrame(root)
# 
frame.pack()
frame.place(x=0,y=0,height=50,width=100)
for i in range(4):
    Button(frame.scrollable_frame, text="%s 示例按钮"%i).pack()
root.mainloop()