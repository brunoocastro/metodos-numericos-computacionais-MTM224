import numpy as np
import matplotlib.pyplot as plt


class IntegracaoNumerica:
    def __init__(self, a, b, n, function):
        self.a = a
        self.b = b
        self.n = n
        self.function = function

    def trapezoidal_rule(self):
        """Implementa a regra dos trapézios para integração numérica."""
        h = (self.b - self.a) / self.n
        x = np.linspace(self.a, self.b, self.n + 1)
        y = self.function(x)
        self.area = (h / 2) * (y[0] + 2 * sum(y[1 : self.n]) + y[self.n])

        print(
            f"Área aproximada sob a curva de {self.a} a {self.b} com {self.n} trapézios: {self.area}"
        )

        return self.area

    def plot(self):
        """Plota a função e a aproximação da integração pelo método dos trapézios."""
        x = np.linspace(self.a, self.b, 1000)
        y = self.function(x)

        plt.plot(x, y, "b", label="f(x)")

        # Pontos utilizados na regra dos trapézios
        x_trap = np.linspace(self.a, self.b, self.n + 1)
        y_trap = self.function(x_trap)

        # Plotando os trapézios
        for i in range(self.n):
            plt.fill(
                [x_trap[i], x_trap[i], x_trap[i + 1], x_trap[i + 1]],
                [0, y_trap[i], y_trap[i + 1], 0],
                "r",
                edgecolor="r",
                alpha=0.3,
            )

        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Método dos Trapézios")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    a = 1
    b = 2
    n = 25  # Número de subintervalos

    def func(x):
        return np.sqrt(x)

    integracao = IntegracaoNumerica(a, b, n, func)

    integracao.trapezoidal_rule()

    integracao.plot()
