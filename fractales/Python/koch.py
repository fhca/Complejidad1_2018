# encoding: latin-1

from Tkinter import *
import math


def koch(e):
    """ Devuelve arreglo de vértices luego de una iteración de Koch. """
    r3=math.sqrt(3)
    r=[]
    a=e[0]
    for b in e[1:]:
        r.append(a)
        x1=a[0]*2./3.+b[0]/3.
        y1=a[1]*2./3.+b[1]/3.
        x2=(b[1]-a[1])/(2.0*r3)+(b[0]+a[0])/2.0
        y2=(b[1]+a[1])/2.0+(a[0]-b[0])/(2.0*r3)
        x3=a[0]/3.+b[0]*2./3.
        y3=a[1]/3.+b[1]*2./3.
        r.append((x1,y1))
        r.append((x2,y2))
        r.append((x3,y3))
        a=b
    r.append(e[-1])
    return r


def pinta(e):
    canvas = Canvas(width=1010, height=760, bg='white')  
    canvas.pack(expand=YES, fill=BOTH)                  
    canvas.create_polygon(*e, fill="red", outline="black",width=2)
    mainloop()

def main():
    e=[(175,360),(305,10),(405,360),(175,360)]
    #e=[(175,360),(305,10)]
    #e.reverse()
    for i in xrange(8):
        e=koch(e)
    pinta(e)

if __name__=="__main__":
    main()
