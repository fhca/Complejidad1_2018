# encoding: utf8

import numpy as np
from bokeh.plotting import figure, show


def dendrita(n=1000):
    """Dendrita con n elementos"""
    delta = 1e-1  # distancia para considerar dos elementos "cercanos"
    e = np.random.rand(2 * n).reshape(-1, 2) * 10 - 5  # elementos moviles inician en pos aleatorias
    e[0] = (0, 0)  # semilla
    u = 1  # cuantos elementos están fijos
    fig = figure()
    i = u
    r = 1e-3
    while u < n:
        p = e[i]
        for f in e[:u]:  # fijos
            if np.linalg.norm(f - p) < delta:
                e[u], e[i] = e[i], e[u]  # fija
                u += 1  # aumenta cuenta de fijos
                break
        theta = np.random.rand(1)[0] * np.pi + np.pi / 2 + \
                np.arctan2(e[i][1], e[i][0])
        e[i] += r * np.array((np.cos(theta), np.sin(theta)))
        i += 1
        if i == n:
            i = u
            if u % 10 == 0:
                print(u)
    fig.circle(*e.T, radius=delta, alpha=.5)
    show(fig)


dendrita()
