from tkinter import *
from tkinter import ttk

class Mainapp(Tk):
    entrada = None
    tipoUnidad = None
    __temperaturaAnt = ""
    def __init__(self):
        Tk.__init__(self)
        self.title("Termómetro")
        self.geometry("200x150")
        self.configure(bg="#ECECEC")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature)
        self.tipounidad = StringVar(value="F")
        
        self.createLayout()
    
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text="Celsius", variable=self.tipounidad, value="C", command=self.selected).place(x=20, y=65)
        self.rb2 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipounidad, value="F", command=self.selected).place(x=20, y=85)
        
        
    def start(self):
        self.mainloop()
    def validateTemperature(self, *args):
        nuevoValor = self.temperatura.get()
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnt)
    
    def selected(self, *args):
        resultado = 0
        tipounidad = self.tipounidad.get()
        grados = float(self.temperatura.get())
        
        if tipounidad == "F":
            resultado = grados * 9/5 + 32
        elif tipounidad == "C":
            resultado = (grados -32) * 5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)
        
if __name__ == '__main__':
    app = Mainapp()
    app.start
