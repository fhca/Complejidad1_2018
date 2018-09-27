import numpy as np
from bokeh.plotting import figure, show
#from matplotlib.pyplot import figure, show, plot

class Ifs:
    def __init__(self, despls=0., escalas=1 / 3, angulos=0, n=0):
        """Sistema de funciones iteradas.
            La función f_i viene dada por el despls_i, la escalas_i y el angulos_i

            n funciones
            si algun otro param es escalar, lo convierte en arreglo de n elementos
            si algun elemento es lista de tamaño mayor a n, toma sólo los 1ros n,
            si algun elemento es lista de tamaño menor a n, completa repitiendo el
            último elemento.
            Si no se dá n, esta será la longitud del arreglo mas largo dado o 0,
            en caso de no darse arreglos.
            self.despls, self.escalas, self.angulos acabarán siendo arreglos del
            mismo tamaño.
            """
        "ajusta el valor de n, de no indicarse."
        self.despls = self.escalas = self.angulos = []
        if n == 0:
            if isinstance(despls, (list, np.ndarray)):
                n = len(despls)
            if isinstance(escalas, (list, np.ndarray)):
                n = len(escalas) if n < len(escalas) else n
            if isinstance(angulos, (list, np.ndarray)):
                n = len(angulos) if n < len(angulos) else n
        if isinstance(despls, (list, np.ndarray)):
            largo = len(despls)
            if n > largo:
                self.despls = np.array(despls + despls[-1] * (n - largo))
            elif largo > n:
                self.despls = np.array(despls[:n])
            else:
                self.despls = np.array(despls)
        if isinstance(escalas, (list, np.ndarray)):
            largo = len(escalas)
            if n > largo:
                self.escalas = np.array(escalas + escalas[-1] * (n - largo))
            elif largo > n:
                self.escalas = np.array(escalas[:n])
            else:
                self.escalas = np.array(escalas)
        if isinstance(angulos, (list, np.ndarray)):
            largo = len(angulos)
            if n > largo:
                self.angulos = np.array(angulos + angulos[-1] * (n - largo))
            elif largo > n:
                self.angulos = np.array(angulos[:n])
            else:
                self.angulos = np.radians(np.array(angulos))
        if isinstance(despls, (complex, float, int)):
            self.despls = np.repeat([despls], n)
        if isinstance(escalas, (complex, float, int)):
            self.escalas = np.repeat([escalas], n)
        if isinstance(angulos, (complex, float, int)):
            self.angulos = np.repeat([angulos], n)
        self.n = n

    def append(self, d=0j, e=1 / 3, a=0):
        """d=desplazamiento(x+yj), e=escala(x+yj), a=angulo(x+yj)radianes."""
        self.despls = np.append(self.despls, d)
        self.escalas = np.append(self.escalas, e)
        self.angulos = np.append(self.angulos, a)
        self.n += 1
        return self

    def grafica(self, datos):
        orb = np.zeros_like(datos, dtype=np.complex64)

        def _evalua(i, _):
            si = int(np.trunc(datos[i] * self.n))
            si = si if si < self.n else si - 1
            d, e, a = self.despls[si], self.escalas[si], self.angulos[si]
            m = complex(np.cos(a), np.sin(a))
            orb[i + 1] = e * m * orb[i] + d  # escala no aplica a despls; rot==mult por complejo m
            return i + 1

        evalua = np.frompyfunc(_evalua, 2, 1)
        evalua.accumulate(np.arange(len(datos), dtype=np.int64), dtype=np.object).astype(np.complex64)
        #p = figure(plot_width=1000, plot_height=int(1000*np.sqrt(3) / 6))  # escalas para Koch
        p = figure(plot_width=700, plot_height=700)  # escalas para Koch
        #p = figure()

        p.cross(orb.real, orb.imag, size=1)
        #plot(orb.real, orb.imag)

        # show(p)
        return p


def uniforme(n):
    """n datos con distribución uniforme."""
    return np.random.rand(n)


def normal(n):
    """n datos con distribución normal (normalizada a [0,1))."""
    r = np.random.randn(n)
    m, M = np.min(r), np.max(r)
    return (r - m) / (M - m)

def normaliza(serie):
    """manda los datos al [0,1)"""
    m, M = np.min(serie), np.max(serie)+1e-10
    return (serie - m) / (M - m)


def logistica(n, r=4):
    """Orbita de la func logística tras 10000 iteraciones descartadas."""
    evalua = np.frompyfunc(lambda x, _: r * x - r * x * x, 2, 1)
    x0 = evalua.accumulate(np.full((10000,), .2), dtype=np.object).astype(np.float)[-1]
    return evalua.accumulate(np.full((n,), x0), dtype=np.object).astype(np.float)


def ejemplos():
    aleatorios = uniforme(100000)

    #sierp = Ifs([0, 1 + 2j, 2], escalas=1 / 2)
    #show(sierp.grafica(logistica(10000)))

    # menger = Ifs([0, 1, 2, 1j, 2j, 1 + 2j, 2 + 1j, 2 + 2j], escalas=1 / 3)
    # show(menger.grafica(aleatorios))
    #
    menger2 = Ifs([0, 1, 2, 1 + 1j, 1 + 2j], escalas=1 / 3)
    show(menger2.grafica(aleatorios))
    #
    # menger3 = Ifs([2, 1j, 1 + 1j, 2j, 1 + 2j], escalas=1 / 3)
    # show(menger3.grafica(aleatorios))
    #
    # # Cantor
    # show(Ifs([2, 2j], escalas=1 / 3).grafica(aleatorios))
    #
    # koch = Ifs([0, 1 / 3, complex(1 / 2, np.sqrt(3) / 6), 2 / 3], escalas=1 / 3, angulos=[0, 60, 300, 0])
    # show(koch.grafica(aleatorios))
    #
    # caos = Ifs([complex(1 / 4, np.sqrt(3) / 4), 0, 1 / 2], escalas=1 / 2, angulos=0)
    # show(caos.grafica(aleatorios))
    #
    # barnsley = Ifs([0, 1.6j, 1.6j, .44j], escalas=[.16j, .85, .328, .328], angulos=[0, -2.7, 52.434, -52.434])
    # show(barnsley.grafica(aleatorios))
    #
    # tree = Ifs([0, 1j, 1j], [1 / 2, 2 / 5, 2 / 3], [0, 45, -60])
    # show(tree.grafica(aleatorios))
    #
    # septs = Ifs([1, -1, 1j, -1j], 3 / 7)
    # show(septs.grafica(aleatorios))


def n_agono(n):
    """Vértices de un n-agono de radio 1."""
    a = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.cos(a) + np.sin(a) * 1j


círculo = [n_agono(100000) / 2, 1/2]

#ejemplos()
show(Ifs(*círculo).grafica(logistica(1000000)))
# show(Ifs(n, escalas=1 / 2).grafica(normal(100000)))

#p = Ifs(círculo, escalas=1 / 2).grafica(logistica(100000))
#p.circle(2 * n.real, 2 * n.imag, color="red", size=2)
#show(p)

# show(Ifs(n, escalas=.5).grafica(logistica(100000)))

sierpinsky = [[0, 1 + 2j, 2], 1/2]
menger = [[0, 1, 2, 1j, 2j, 1 + 2j, 2 + 1j, 2 + 2j], 1 / 3]

#show(Ifs(*sierpinsky).grafica(uniforme(100000)))

#import pandas as pd
#datos = pd.read_csv("~/Desktop/Pachuca Sep2018/PCM/PCM90SUE_F7.txt", header=None)[0][1377000:1387000]
#show(Ifs(*círculo).grafica(normaliza(datos)))

#ejemplos()