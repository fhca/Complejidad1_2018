#encoding: utf-8

from Tkinter import *
from julia import *

class Mandelbrot(Julia):
    def __init__(self, master=None):
        Julia.__init__(self, master)
        self.ireal=-2.4
        self.dreal=0.8
        self.breal=-1.25
        self.treal=1.25

    def creaPartes(self):
        self.extras()

    def escapa(self):
        si=self.si
        ve=self.valor_escape
        iteraciones=self.iteraciones
        canvas=self.canvas
        colores=self.colores
        w,h=self.w,self.h
        ireal,dreal,breal,treal=self.ireal,self.dreal,self.breal,self.treal
        for i in xrange(0,w,si):
            for j in xrange(0,h,si):
                zre=0.
                zim=0.
                cre=self.lineal(i,0,w-1,ireal,dreal)
                cim=self.lineal(j,0,h-1,breal,treal)
                try:
                    for it in xrange(iteraciones):
                        (zre,zim)=(zre*zre-zim*zim+cre,2.*zre*zim+cim)
                        if zre*zre+zim*zim>ve:
                            color=colores[iteraciones-it]
                            canvas.create_rectangle(i,j, i+si,j+si,
                                            fill=color, width=0, tag="fractal")
                            break
                except ValueError:
                    pass
        return 0

def main():
    Mandelbrot().mainloop()

if __name__=="__main__":
    main()
