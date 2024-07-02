import tkinter as tk
from tkinter import ttk

class Window(tk.Tk): # 自訂class Window()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("My created Window") #設定title 文字
        self.geometry("500x500") #設定geometry 視窗大小
        
        # btn1:ttk.Button=ttk.Button(self,text="Top") #建立ttk.Button 的實體
        # btn1.pack()

        ttk.Button(self,text="Top").pack() #簡化

        # btn2:ttk.Button=ttk.Button(self,text="Middle")
        # btn2.pack()

        ttk.Button(self,text="Middle").pack()

        # btn3:ttk.Button=ttk.Button(self,text="Button")
        # btn3.pack()

        ttk.Button(self,text="Button").pack()


if __name__=="__main__":
    window:Window=Window() #自訂變數 window
    window.mainloop()

 