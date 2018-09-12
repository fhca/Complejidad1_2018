import numpy as np
from bokeh.plotting import figure, show


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
            if isinstance(despls, list):
                n = len(despls)
            if isinstance(escalas, list):
                n = len(escalas) if n < len(escalas) else n
            if isinstance(angulos, list):
                n = len(angulos) if n < len(angulos) else n
        if isinstance(despls, list):
            largo = len(despls)
            if n > largo:
                self.despls = np.array(despls + despls[-1] * (n - largo))
            elif largo > n:
                self.despls = np.array(despls[:n])
            else:
                self.despls = np.array(despls)
        if isinstance(escalas, list):
            largo = len(escalas)
            if n > largo:
                self.escalas = np.array(escalas + escalas[-1] * (n - largo))
            elif largo > n:
                self.escalas = np.array(escalas[:n])
            else:
                self.escalas = np.array(escalas)
        if isinstance(angulos, list):
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

    def grafica(self, alea):
        orb = np.zeros_like(alea, dtype=np.complex64)

        def _evalua(i, _):
            x, y = orb[i].real, orb[i].imag
            si = int(np.trunc(alea[i] * self.n))
            si = si if si < self.n else si - 1
            d, e, a = self.despls[si], self.escalas[si], self.angulos[si]
            c, s = np.cos(a), np.sin(a)
            orb[i + 1] = e * complex(c * x - s * y, s * x + c * y) + d
            return i + 1

        evalua = np.frompyfunc(_evalua, 2, 1)
        evalua.accumulate(np.arange(len(alea), dtype=np.int64), dtype=np.object).astype(np.complex64)
        # p = figure(plot_width=1000, plot_height=int(1000*np.sqrt(3) / 6))
        p = figure(plot_width=700, plot_height=700)
        p.cross(orb.real, orb.imag, size=1)
        show(p)


aleatorios = np.random.rand(100000)

# sierp = Ifs([0, 1 + 2j, 2], escalas=1 / 2)
# sierp.grafica(aleatorios)

# menger = Ifs([0, 1, 2, 1j, 2j, 1 + 2j, 2 + 1j, 2 + 2j])
# menger.grafica(aleatorios)

# menger2 = Ifs([0, 1, 2, 1 + 1j, 1 + 2j])
# menger2.grafica(aleatorios)

# menger3 = Ifs([2, 1j, 1 + 1j, 2j, 1 + 2j])
# menger3.grafica(aleatorios)

# Cantor
# Ifs([2, 2j]).grafica(aleatorios)

# koch = Ifs([0, 1, complex(1.5, np.sqrt(3) / 2), 2], angulos=[0, 60, -60, 0])
# koch.grafica(aleatorios)

# koch = Ifs([0, 1 / 3, complex(1 / 2, np.sqrt(3) / 6), 2 / 3], angulos=[0, 60, 300, 0])
# koch.grafica(aleatorios)

# caos = Ifs([complex(1 / 4, np.sqrt(3) / 4), 0, 1 / 2], 1/2, 0 )
# caos.grafica(aleatorios)

# barnsley = Ifs([0, 1.6j, 1.6j, .44j], escalas=[.1j, .7, .3, .3], angulos=[0,10, 30, -30])
# barnsley.grafica(aleatorios)

#tree = Ifs([0, 1j, 1j], [1 / 2, 2 / 5, 2 / 3], [0, 45, -60])
#tree.grafica(aleatorios)

# septs = Ifs([1, -1, 1j, -1j], 3/7)
# septs.grafica(aleatorios)

