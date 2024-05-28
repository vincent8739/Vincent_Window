import tkinter as tk
from tkinter import ttk

def get_names() ->list[str]:
    with open("names.txt", encoding="utf-8") as file_obj:
         content:list[str]=file_obj.read()
    names:list[str]=content.split() #區域變數
    return names
    # len(names)
    # print(len(names))
    # for name in names:
    #     print(name)

# if __name__=="__main__":
#     names:list[str]=get_names() #文件變數 相同名字不衝突
#     window:tk.Tk=tk.Tk()
#     window.title("我建立的視窗畫面")
#     window.mainloop()

# class Window(tk.Tk):
#     def __init__(self,title:str="視窗建立",**kwargas)
#         super().__init__(**kwargas) #執行父類別
#         self.title(title)

# if __name__=="__main__":
#      names:list[str]=get_names() #文件變數 相同名字不衝突
#      window:Window=Window()
#      window.mainloop()


class Window(tk.Tk):
    def __init__(self,title:str="Hello! Tkinter!",**kwargs):
        super().__init__(**kwargs)
        #多做一些事
        self.title(title)
        label:ttk.Label=ttk.Label(self,
                                  text="Hello, How are you",
                                  font=("Arial",50,"bold"),
                                  foreground="#f00"
                                  )
        
        label.pack(padx=100,pady=40)

if __name__ == '__main__':
    names:list[str] = get_names()
    window:Window = Window(title="這是的第一個GUI程式") 
    window.mainloop()