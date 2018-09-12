# encoding: utf-8

"""
julia.py - Programa para dibujar fractales de Julia variando la constante.

Autor: Felipe Contreras / Felipe.Contreras@uacm.edu.mx
Licencia: GPL
"""

from Tkinter import *


class Julia(Frame):
    def __init__(self, master=None):
        """ Define algunos datos iniciales. """
        Frame.__init__(self, master)
        self.grid()  # usar modelo grid para situar botones y ventana
        self.w = 400  # ancho de ventana de dibujo
        self.h = 350  # alto de ventana de dibujo
        self.si = 3  # tamaÃ±o del punto
        self.ireal = -2.  # el extremo izquierdo de la ventana en coord reales
        self.dreal = 2.  # idem para extremo derecho  (maxima coord x)
        bt = (self.dreal - self.ireal) * self.h / float(self.w)
        self.breal = -bt / 2.  # idem para extremo inferior
        self.treal = bt / 2.  # idem para extremo superior
        self.c = (0, 0)  # constante "c" en "z=z**2+c", variada interactiv.
        # self.ij=[] # Lista de (i,j,ir,jr), coordenadas i,j enteras y reales
        # de toda la ventana de dibujo. Ineficiente en memoria, pero evita hacer
        # cálculos.
        # conf fractal
        self.iteraciones = 20
        self.valor_escape = 4
        # PALETAS multicolor
        self.colores = ["#" + ("00" + "%x" % i)[-3:] for i in xrange(0, 4096, 4096 / self.iteraciones)]
        # azules
        # self.colores=["#"+("0"*12+"%x"%(x**2))[-12:] for x in xrange(1024,1,-5)]
        self.click = None
        # partes de la ventana
        self.creaPartes()

    def creaPartes(self):
        # escalas
        self.re = Scale(self, from_=-2, to=2, orient=HORIZONTAL,
                        resolution=0.001, label="real", length=300,
                        command=self.modifica_re)
        self.re.grid(row=1, column=0)
        self.im = Scale(self, from_=-2, to=2, orient=HORIZONTAL,
                        resolution=0.001, label="imaginaria", length=300,
                        command=self.modifica_im)
        self.im.grid(row=1, column=1)
        self.extras()

    def extras(self):
        # canvas
        self.canvas = Canvas(self, width=self.w, height=self.h, bg='black')
        self.canvas.grid(row=0, column=0, columnspan=4)
        self.tampto = Scale(self, from_=1, to=10, orient=HORIZONTAL,
                            resolution=1, label="tamaño punto", command=self.modifica_tampto)
        self.tampto.bind("<ButtonRelease-1>", self.pinta)
        self.tampto.set(self.si)
        self.tampto.grid(row=1, column=2)
        # redibuja
        self.redibuja = Button(self, text="Redibuja", command=self.pinta)
        self.redibuja.grid(row=1, column=3)
        # salir
        self.botonSalir = Button(self, text="q=Salir", command=self.salir)
        self.botonSalir.grid(row=2, column=0)
        # binds para el ratÃ³n
        c = self.canvas
        c.bind("<Button-1>", self.onClick1)
        c.bind("<B1-Motion>", self.onMotion1)
        c.bind("<ButtonRelease-1>", self.onRelease1)
        c.bind("<ButtonRelease-3>", self.onRelease3)
        c.bind("<KeyPress-q>", self.salir)
        c.focus_set()

    def lineal(self, x, a0, b0, a1, b1):
        return float(x - a0) * (b1 - a1) / (b0 - a0) + a1

    def modifica_re(self, param):
        self.c = (float(param), self.c[1])

    def modifica_im(self, param):
        self.c = (self.c[0], float(param))

    def modifica_tampto(self, param):
        self.si = int(param)

    def escapa(self):
        si = self.si
        (cre, cim) = self.c
        ve = self.valor_escape
        iteraciones = self.iteraciones
        canvas = self.canvas
        colores = self.colores
        w, h = self.w, self.h
        ireal, dreal, breal, treal = self.ireal, self.dreal, self.breal, self.treal
        for i in xrange(0, w, si):
            for j in xrange(0, h, si):
                zre = self.lineal(i, 0, w - 1, ireal, dreal)
                zim = self.lineal(j, 0, h - 1, breal, treal)
                for it in xrange(iteraciones):
                    (zre, zim) = (zre * zre - zim * zim + cre, 2. * zre * zim + cim)
                    if zre * zre + zim * zim > ve:
                        color = colores[iteraciones - it]
                        canvas.create_rectangle(i, j, i + si, j + si,
                                                fill=color, width=0, tag="fractal" + str(si))
                        break
        return 0

    def pinta(self, param=0):
        # borra dibujo previo
        self.canvas.delete("fractal")
        self.escapa()

    def onClick1(self, event):
        (x, y) = self.click = event.x, event.y
        self.seleccionando = self.canvas.create_rectangle(x, y, x, y, outline="yellow", dash=(4, 4), tag="selec")

    def onMotion1(self, event):
        if self.seleccionando:
            x, y = self.click
            x1, y1 = self.clickt = event.x, event.y
            self.canvas.coords("selec", x, y, x1, y1)

    def minmax(self, a, b):
        return (a, b) if a <= b else (b, a)

    def onRelease1(self, event):
        w = self.w;
        h = self.h
        self.canvas.delete("selec")
        a, b = self.click
        c, d = self.clickt
        x, x1 = self.minmax(a, c)
        y, y1 = self.minmax(b, d)
        fe = w / float(h)
        # ajusta dimensiones mas grandes para conservar proporciones de ventana
        if x1 - x <= y1 - y:
            yi = (y + y1) / 2. - (x1 - x) / fe / 2.
            yd = (y + y1) / 2. + (x1 - x) / fe / 2.
            y = yi
            y1 = yd
        else:
            xi = (x + x1) / 2. - (y1 - y) * fe / 2.
            xd = (x + x1) / 2. + (y1 - y) * fe / 2.
            x = xi
            x1 = xd
        if not (x, y) == (x1, y1):
            ireal = self.lineal(x, 0, w - 1, self.ireal, self.dreal)
            breal = self.lineal(y, 0, h - 1, self.breal, self.treal)
            dreal = self.lineal(x1, 0, w - 1, self.ireal, self.dreal)
            treal = self.lineal(y1, 0, h - 1, self.breal, self.treal)
            self.ireal = ireal
            self.breal = breal
            self.dreal = dreal
            self.treal = treal
            self.pinta()

    def onRelease3(self, event):
        e = 1.5
        x = self.lineal(event.x, 0, self.w - 1, self.ireal, self.dreal)
        y = self.lineal(event.y, 0, self.h - 1, self.breal, self.treal)
        self.ireal = (self.ireal - x) * e + x
        self.dreal = (self.dreal - x) * e + x
        self.breal = (self.breal - y) * e + y
        self.treal = (self.treal - y) * e + y
        self.pinta()

    def salir(self, event=None):
        self.quit()


def main():
    Julia().mainloop()


if __name__ == "__main__":
    main()
