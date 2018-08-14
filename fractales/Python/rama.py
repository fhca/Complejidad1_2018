#encoding: latin1

import math
from Tkinter import *

reduccion=0.8
semianguloi=25
semiangulod=20
iteraciones=10
asimetria1=1

cost=math.cos(semianguloi*math.pi/180)
sint=math.sin(semianguloi*math.pi/180)
cosf=math.cos(semiangulod*math.pi/180)
sinf=math.sin(semiangulod*math.pi/180)

def rama(hojas):
    h=[]
    for rama in hojas:
        (a,b)=rama
        (x,y)=((b[0]-a[0])*reduccion,(b[1]-a[1])*reduccion)
        b1=(cost*x-sint*y,sint*x+cost*y)
        b2=((cosf*x+sinf*y)*asimetria1,(-sinf*x+cosf*y)*asimetria1)
        h.append((b,(b1[0]+b[0],b1[1]+b[1])))
        h.append((b,(b2[0]+b[0],b2[1]+b[1])))
    return h

def main():
    canvas = Canvas(width=500, height=400, bg='white')  
    canvas.pack(expand=YES, fill=BOTH)
    r=[((250,380),(250,300))]
    h=r[:]
    for i in xrange(iteraciones):
        h=rama(h)
        r.extend(h)
    for ((a,b),(c,d)) in r:
        canvas.create_line(a,b,c,d, fill="green")
    mainloop()

if __name__=="__main__":
    main()
