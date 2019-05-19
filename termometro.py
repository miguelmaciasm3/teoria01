import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")
    
    def convertir(self, grados, tipounidad):
        resultado = 0
        if tipounidad == "F":
            resultado = grados * 9/5 + 32
        elif tipounidad == "C":
            resultado = (grados -32) * 5/9
        else:
            resultado = grados
            print("falla aqui, cenutrio")
        return "{:10.2f}".format(resultado)

class Selector():
    __tipounidad = None
    
    def __init__(self, unidad="C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipounidad = unidad
        
    def custome(self):
        if self.__tipounidad == 'F':
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    def change(self):
        if self.__tipounidad == 'F':
            self.__tipounidad = 'C'
        else:
            self.__tipounidad = 'F'
            
    def unidad(self):
        return self.__tipounidad

class Numberinput():
    __value = 0
    __strvalue = ""
    __position = [0,0]
    __size = [0, 0]
    __pointsCount = 0
    
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)
        
    
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strvalue) < 10 or (event.unicode == '.' and self.__pointsCount == 0):
                self.__strvalue += event.unicode
                self.value(self.__strvalue)
                if event.unicode == '.':
                    self.__pointsCount += 1
                
            elif event.key == K_BACKSPACE:
                if self.__strvalue[-1] == '.':
                    self.__pointsCount -= 1
                self.__strvalue = self.__strvalue[:-1]
                self.value(self.__strvalue)
                
    
    def render(self):
        textBlock = self.__font.render(self.__strvalue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)
    
    def value(self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = float(val)
                self.__strvalue = val
                if '.' in self.__strvalue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass
    
    
    
    def posx(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                    pass
    
    def posy(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                    pass
    
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                    pass
    
    
    def width(self, val=None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
    
    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass

class Mainapp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        
        self.termometro = Termometro()
        self.entrada = Numberinput("termometro")
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
        
        self.selector = Selector()
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    
                    nuevaunidad = self.selector.unidad()
                    
                    temperatura = self.termometro.convertir(grados, nuevaunidad)
                    
                    self.entrada.value(temperatura)
                
                
            #pintamos el fondo de pantalla
            self.__screen.fill((244, 236, 203))
            
            #pintamos el termopmetro en su posicion
            self.__screen.blit(self.termometro.custome, (50, 34))
            #pintamos el cuadro de texto
            #obtenemos rectangulo blanco y foto de texto y lo asignamos a text
            text = self.entrada.render()
            #creamos el rectangulo blanco, con sus datos (posicion y tamaño) text[0]
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0])
            #pintamos la foto del texto (text[1])
            self.__screen.blit(text[1], self.entrada.pos())
            
            #dibujamos el selector
            self.__screen.blit(self.selector.custome(), (112, 153))
            
            pygame.display.flip()
                
        
if __name__ == '__main__':
    pygame.init()
    app = Mainapp()
    app.start()