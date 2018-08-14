#encoding: latin1

import random
from Tkinter import *


K=2
def dendr(c,m,n):
    """ Regresa un arreglo de c posiciones al azar dentro del rango (m,n)"""
    global K
    return [(str(i),random.randrange(m/2-m/K,m/2+m/K), random.randrange(n/2-n/K,n/2+n/K)) for i in xrange(c)]

def cmp(a,b):
    return 1 if b>a else -1 if a>b else 0

def choca(x,y,fijas):
    for (a,b) in fijas:
        if (a-x)*(a-x)+(b-y)*(b-y)<z*z:
            return True
    return False

def paso(d,f,m,n,z):
    global J
    for j,(i,x,y) in enumerate(d):
        #nx=(x+random.randrange(-z,z+1))%m
        #ny=(y+random.randrange(-z,z+1))%n
        r=random.random()*.1
        nx=(m/2*r+(1-r)*x+random.randrange(-z,z+1))%m
        r=random.random()*.1
        ny=(n/2*r+(1-r)*y+random.randrange(-z,z+1))%n
        if choca(nx,ny,f):
            f.append((x,y))
            canvas.itemconfig(i,fill='blue',outline='blue')
            d[j]=(str(J),random.randrange(m/2-m/K,m/2+m/K),random.randrange(n/2-n/K,n/2+n/K))
            canvas.create_oval(x-z,y-z,x+z,y+z, fill='black', tag=str(J))
            J=J+1
        else:
            d[j]=(i,nx,ny)
            canvas.coords(i,nx-z,ny-z,nx+z,ny+z)

m,n=750,750
z=1
d=dendr(150,m,n)
f=[(m/2,n/2)]
J=len(d)

canvas=Canvas(width=m, height=n, bg='white')
canvas.pack(expand=YES, fill=BOTH)

for (i,x,y) in d:
    canvas.create_oval(x-z,y-z,x+z,y+z, fill='black', tag=i)

def itera():
    global d,f,m,n,z
    paso(d,f,m,n,z)
    canvas.after(1, itera)

canvas.after(10, itera)
canvas.bind("<KeyPress-q>", quit)
canvas.focus_set()

mainloop()


