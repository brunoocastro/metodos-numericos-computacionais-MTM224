import numpy as np

import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, functions):
        # rewrite to receive any ammount of functions
        if type(functions) is not list:
            functions = [functions]

        self.functions = functions

    def plot_functions(self, xmin, xmax, num_points=100):
        x_values = np.linspace(xmin, xmax, num_points)

        for index, function in enumerate(self.functions):
            func_y_values = function(x_values)
            plt.plot(x_values, func_y_values, label=f"Função {index} : {function}")

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
    plotter = Plotter([g, h])

    plotter.plot_functions(0.01, 10)
