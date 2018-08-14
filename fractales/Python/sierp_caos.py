#encoding:latin1

from random import *
from tkinter import *

def mitad(a,b,p=1./2.):
    """ Devuelve el punto a*p+b*(1-p). """
    return (a[0]*p+b[0]*(1-p),a[1]*p+b[1]*(1-p))

def itera(actual,vertices):
    azar=choice(vertices)
    return mitad(actual,azar)

def main():
    e=[(10,500),(255,10),(500,500)]
    #e=[(10,10),(500,10),(500,500),(10,500)]
    #e=[(10,10),(500,10),(500,500),(10,500),(250,250)]
    #e=[(10,200),(250,10),(540,200),(380,540),(120,540)]
    canvas = Canvas(width=550, height=550, bg='white')  
    canvas.pack(expand=YES, fill=BOTH)                  
    (x,y)=(0,0)
    t=1
    for i in range(40000):
        (x,y)=itera((x,y),e)
        canvas.create_polygon(x,y,x+t,y,x+t,y+t,x,y+t,fill="blue")
    mainloop()

if __name__=="__main__":
    main()
