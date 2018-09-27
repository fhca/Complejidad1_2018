__author__ = 'fhca'

import numpy as np
from bokeh.plotting import figure, show


def logistica(n, r=4):
    """Orbita de la func logística tras 10000 iteraciones descartadas."""
    evalua = np.frompyfunc(lambda x, _: r * x - r * x * x, 2, 1)
    x0 = evalua.accumulate(np.full((10000,), .2), dtype=np.object).astype(np.float)[-1]
    return evalua.accumulate(np.full((n,), x0), dtype=np.object).astype(np.float)


def feigenbaum(min=3, max=4):
    verticales = 1000
    horizontales = 1000
    p = figure()
    for r in np.linspace(min, max, horizontales):
        p.cross(np.ones(verticales)*r, logistica(verticales, r), size=1)
    show(p)


feigenbaum(3, 4)
