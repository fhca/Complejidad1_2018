__author__ = 'fhca'

import re  # regular expresions
import io
import numpy as np


def estadisticas(libro):
    with io.open(libro, mode='r', encoding="utf-8") as f:
        t = f.readlines()

    words = re.compile(r'\W+')
    letras = re.compile(r'')
    # dots = re.compile(r'\.')

    megalista = []
    for parrafo in t:
        p = parrafo.lower()  # pasa a minúsculas el párrafo
        lista_palabras = words.split(p)
        lista_letras = []
        for palabra in lista_palabras:
            lista_letras.extend(letras.split(palabra))
            ll = []
            for l in lista_letras:
                if l != '':
                    ll.append(l)
            lista_letras = ll
        megalista.extend(lista_letras)
    return megalista

def estadisticas2(libro):
    with io.open(libro, mode='r', encoding="utf-8") as f:
        t = f.readlines()

    words = re.compile(r'\W+')
    letras = re.compile(r'')
    # dots = re.compile(r'\.')

    megalista = []
    for parrafo in t:
        p = parrafo.lower()  # pasa a minúsculas el párrafo
        lista_palabras = words.split(p)
        ll = []
        for l in lista_palabras:
            if l != '':
                ll.append(l)
        lista_palabras = ll
        megalista.extend(lista_palabras)
    return megalista

def cuenta(a):
    d = dict()
    for l in a:
        d[l] = d.get(l, 0) + 1
    return d.items()


res = estadisticas2("L1piedra.txt")

import pylab as plt

plt.figure()

dletras = list(cuenta(res))
dletras.sort(key=lambda pareja: pareja[1], reverse=True)

x, y = np.array(dletras).T
y = y.astype(np.int)
xi = range(len(x))
#plt.xticks(xi, x, rotation=90)
plt.xscale('log')
plt.yscale('log')
#plt.axes([0, len(y), 0, 50000])

plt.plot(xi, y)

plt.show()
