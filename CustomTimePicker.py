
import tkinter as tk
from tkinter.font import Font


class CTPiker(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=1,to=12,wrap=True,textvariable=self.hourstr,width=3,state="readonly",font=Font(family='Helvetica', size=10) )
        self.minstr=tk.StringVar(self,'30')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=3,state="readonly", font=Font(family='Helvetica', size=10,))

        self.itemList=["AM", "PM"]
        self.periodStr = tk.StringVar()
        self.period = tk.Spinbox(self, values=self.itemList, textvariable=self.periodStr ,width=3,state="readonly", font=Font(family='Helvetica', size=10))

        self.hour.grid()
        self.min.grid(row=0,column=1)
        self.period.grid(row=0,column=2)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="12" else 1)
        self.last_value = self.minstr.get()



    def getTime(self):
        _hour = tk.StringVar()
        if len(self.hourstr.get()) == 2:_hour = self.hourstr.get()
        else: _hour = '0' + self.hourstr.get()

        _minutes = tk.StringVar()
        if len(self.minstr.get()) == 2: _minutes = self.minstr.get()
        else:_minutes = '0' + self.minstr.get()
        return _hour+":"+_minutes +" "+ self.periodStr.get()
