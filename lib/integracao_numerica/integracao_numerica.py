import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """Defina aqui a função que você deseja integrar."""
    return np.sqrt(x)


def trapezoidal_rule(a, b, n, f):
    """Implementa a regra dos trapézios para integração numérica."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    area = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])
    return area


def plot_trapezoidal_integration(a, b, n, f):
    """Plota a função e a aproximação da integração pelo método dos trapézios."""
    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.plot(x, y, "b", label="f(x)")

    # Pontos utilizados na regra dos trapézios
    x_trap = np.linspace(a, b, n + 1)
    y_trap = f(x_trap)

    # Plotando os trapézios
    for i in range(n):
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

    area = trapezoidal_rule(a, b, n, f)
    print(f"Área aproximada sob a curva de {a} a {b} com {n} trapézios: {area}")

    plot_trapezoidal_integration(a, b, n, f)
