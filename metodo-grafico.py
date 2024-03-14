import math
from Plotter import Plotter


# Exemplo de funções
def g(x):
    return x


def h(x):
    return 2 / x


# Instanciando a classe e plotando os gráficos
plotter = Plotter(g, h)
plotter.plot_functions(-10, 10)

# TODO -> Estudar como renderizar exp(x)
# def ex3gx(x):
#     return 4 * math.cos(x)


# def ex3hx(x):
#     return math.exp(2 * x)


# plotter = Plotter(ex3gx, ex3hx)
# plotter.plot_functions(-10, 10)

