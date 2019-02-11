from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        # return super().__init__(master=master, cnf=cnf, **kw)

    # pack()方法把组件添加到主容器中
    def createWidgets(self):
        self.helloLabel = Label(self, text='hello world')
        self.helloLabel.pack()
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.helloBtn=Button(self,text='hello',command=self.hello)
        self.helloBtn.pack()
        self.quitBtn = Button(self, text='quit', command=self.quit)
        self.quitBtn.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello %s'%name)

app=Application()       
# 设置主题
app.master.title('hello world')
# 主消息循环
app.mainloop()
