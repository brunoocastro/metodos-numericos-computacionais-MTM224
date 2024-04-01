import numpy as np
from Plotter import Plotter


# Exemplo de funções
def g(x):
    return x


def h(x):
    return 2 / x


# Instanciando a classe e plotando os gráficos
plotter = Plotter([g, h])
plotter.plot_functions(1, 10)


def ex3gx(x):
    return 4 * np.cos(x)


def ex3hx(x):
    return np.exp(2 * x)


plotter = Plotter([ex3gx, ex3hx])
plotter.plot_functions(0.5, 0.75)
