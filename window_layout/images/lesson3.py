import tkinter as tk
from tkinter import ttk

class Window(tk.Tk): # 自訂class Window()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("My created Window") #設定title 文字
        self.geometry("300x300") #設定geometry 視窗大小
        
        ttk.Button(self,text="Top").pack(side="right") #建立ttk.Button 的實體 

        ttk.Button(self,text="Middel").pack(side="left")

        ttk.Button(self,text="Button").pack(side="left")


if __name__=="__main__":
    window:Window=Window() #自訂變數 window
    window.mainloop()

 