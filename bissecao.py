import time

from matplotlib import pyplot as plt


class Bissecao:
    def __init__(self, a, b, f, error=0.0001):
        self.a = [a]
        self.b = [b]
        self.f = f
        self.max_error = error

    def get_medium_point(self):
        return (self.a[-1] + self.b[-1]) / 2

    def get_f_medium_point(self):
        return self.f(self.get_medium_point())

    def calculate_interval(self):
        if self.get_f_medium_point() * self.f(self.a[0]) < 0:
            self.a.append(self.a[-1])
            self.b.append(self.get_medium_point())
        else:
            self.a.append(self.get_medium_point())
            self.b.append(self.b[-1])

    def calculate_root(self):
        while abs(self.b[-1] - self.a[-1]) > self.max_error:
            self.calculate_interval()
        return self.get_medium_point()

    def show_method_progression(self):
        fig, ax = plt.subplots()

        # Para cada posição do array, plotar os 2 pontos e as linhas entre eles
        for i in range(len(self.a)):
            ax.plot([self.a[i], self.b[i]], [i, i], "bo-")
            ax.plot([self.a[i], self.b[i]], [i, i], "r-")

        ax.set_yticks(range(len(self.a)))
        ax.set_yticklabels([f"[{i+1}]" for i in range(len(self.a))])
        # ax.set_yticklabels([f"Iteration {i+1}" for i in range(len(self.a))])
        ax.set_xlabel("x")
        ax.set_title("Bisection Method Progression")
        ax.grid(True)
        # plt.savefig("bisection_progression.png")
        plt.show()


if __name__ == "__main__":
    bissecao = Bissecao(0, 10, lambda x: x**2 - 2, 1e-10)
    start_time = time.time()
    result = bissecao.calculate_root()
    finish_time = time.time()

    print(
        f"Resultado: {result} \nTempo da resolução: \
          {finish_time - start_time} seconds"
    )

    bissecao.show_method_progression()
