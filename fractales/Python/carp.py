from bokeh.plotting import figure, show
import numpy as np


def carp(h):
    """Devuelve arreglo de vértices luego de una iteración de Carp. """
    l = []
    for e in h:
        (a, b, c, d) = e
        r = 1 / 3
        abb = (1 - r) * a + r * b
        aab = (1 - r) * b + r * a
        bcc = (1 - r) * b + r * c
        bbc = (1 - r) * c + r * b
        cdd = (1 - r) * c + r * d
        ccd = (1 - r) * d + r * c
        add = (1 - r) * a + r * d
        aad = (1 - r) * d + r * a
        aa = (1 - r) * add + r * bcc
        bb = (1 - r) * bcc + r * add
        cc = (1 - r) * bbc + r * aad
        dd = (1 - r) * aad + r * bbc
        l.append([a, abb, aa, add])  # SO
        l.append([abb, aab, bb, aa])  # S
        l.append([aab, b, bcc, bb])  # SE
        l.append([bb, bcc, bbc, cc])  # E
        l.append([cc, bbc, c, cdd])  # NE
        l.append([dd, cc, cdd, ccd])  # N
        l.append([aad, dd, ccd, d])  # NO
        l.append([add, aa, dd, aad])  # O
    return np.array(l)


def pinta(h):
    """h es un arreglo de polígonos."""
    f = figure()
    xx, yy = h.transpose(2, 0, 1)  # separa x, y
    for x, y in zip(xx, yy):  # pinta polígonos individuales
        f.patch(x, y, alpha=0.5, color="blue", )
    show(f)


def main():
    e = np.array((((0, 0), (1, 0), (1, 1), (0, 1)),))
    for i in range(3):
        e = carp(e)
    pinta(e)


if __name__ == "__main__":
    main()
