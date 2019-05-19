from tkinter import *
from tkinter import ttk

class Mainapp(Tk):
    size = "640x480"
    def __init__(self):
        Tk.__init__(self)
        self.geometry(self.size)
        self.title("ventana ejemplo")
        self.configure(bg = "red")
        
    def start(self):
        self.mainloop()
if __name__ == '__main__':
    app = Mainapp()
    app.start()