# encoding: latin-1

from Tkinter import *
import math

def sierp(e):
    """ Devuelve arreglo de vértices luego de una iteración de
    Sierpinski. """
    r=[]
    while e:
        (a,b,c)=e[:3]
        ab=((a[0]+b[0])/2.,(a[1]+b[1])/2.)
        bc=((b[0]+c[0])/2.,(b[1]+c[1])/2.)
        ac=((a[0]+c[0])/2.,(a[1]+c[1])/2.)
        #triángulo con vértice en a
        r.extend([a,ab,ac])
        #triángulo con vértice en b
        r.extend([b,bc,ab])
        #triángulo con vértice en c
        r.extend([c,ac,bc])
        del e[:3]
    return r


def pinta(e):
    canvas = Canvas(width=1010, height=750, bg='white')  
    canvas.pack(expand=YES, fill=BOTH)                  
    while e:
        canvas.create_polygon(*e[:3],  fill="blue",outline="blue",width="1")
        del e[:3]
    mainloop()

def chivito():
    e=[(0,540),(400,0),(800,540)]
    for i in xrange(3):
        e=sierp(e)
    pinta(e)

if __name__=="__main__":
    chivito()
