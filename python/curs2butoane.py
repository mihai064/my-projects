import tkinter
from tkinter import ttk
from tkinter import Tk

class Root (Tk):
 def _init_ (self):
     super (Root, self)._init_ ()
     self.title ("Enter Name")
     self.minsize (640,400)
     self.wm_iconbitmap ('icon.ico')
     
     self.initUI()

 def clickMe (self):
     seld.label.configure (text= "Hello" + self.name.get())

 def initUI(self):
      self.name = StringVar()

     self.label = ttk.Label (self, text = "Enter your name")
     self.label.grid(column = 0, row =1 )


     self.textbox = ttk.Entry (self, width = 20, textvariable = self.name)
     self.textbox.grid (column = 0, row = 1)

     self.button = ttk.Button (self, text = "Click me", self.clickMe) 
     self.button.grid (row = 0, column = 2)
button.bind("<ButtonRelease-1>", _init_)

root = Root ()
root.mainloop ()


