import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, func1, func2):
        self.func1 = func1
        self.func2 = func2

    def plot_functions(self, xmin, xmax, num_points=100):
        x_values = np.linspace(xmin, xmax, num_points)
        y_values_func1 = self.func1(x_values)
        y_values_func2 = self.func2(x_values)

        plt.plot(x_values, y_values_func1, label="Func1")
        plt.plot(x_values, y_values_func2, label="Func2")

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráficos das Funções")
        plt.legend()
        plt.grid(True)
        plt.show()


# Se a função for executada diretamente, não será executada a classe, apenas o código dentro dela.
if __name__ == "__main__":

    # Exemplo de funções
    def g(x):
        return x

    def h(x):
        return 2 / x

    # Instanciando a classe e plotando os gráficos
    plotter = Plotter(g, h)
    plotter.plot_functions(-10, 10)
