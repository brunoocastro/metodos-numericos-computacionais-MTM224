import random
import time
import numpy as np

from matplotlib import pyplot as plt

from Plotter import Plotter


class Bissecao:
    def __init__(self, f, a, b, error=0.0001):
        self.a = [a]
        self.b = [b]
        self.pm = ["-"]
        self.f = f
        self.fpm = ["-"]
        self.epsilon = error

    @staticmethod
    def has_solution(func, step=0.005):
        random_a = random.random() * 10
        random_b = random.random() * -10

        lower_interval = random_a
        higher_interval = random_b

        print(higher_interval, lower_interval)

        while func(higher_interval) * func(lower_interval) < 0:
            higher_interval -= step
            lower_interval += step
            print(higher_interval, lower_interval)

        return lower_interval, higher_interval

    def estimate_iterations(self):
        higherThan = (np.log(self.b[0] - self.a[0]) - np.log(self.epsilon)) / np.log(2)

        N = int(np.ceil(higherThan))

        print(f"O número de iterações N é de {N}")

        return

    def get_medium_point(self):
        return (self.a[-1] + self.b[-1]) / 2

    def get_f_medium_point(self):
        return self.f(self.get_medium_point())

    def calculate_interval(self):
        pm = self.get_medium_point()
        self.pm.append(pm)

        fpm = self.get_f_medium_point()
        self.fpm.append(fpm)
        if fpm * self.f(self.a[0]) < 0:
            self.a.append(self.a[-1])
            self.b.append(pm)
        else:
            self.a.append(pm)
            self.b.append(self.b[-1])

    def calculate_root(self):
        finished_by_image = False
        finished_by_domain = False

        while not finished_by_image and not finished_by_domain:
            self.calculate_interval()

            if abs(self.b[-1] - self.a[-1]) < self.epsilon:
                finished_by_domain = True

            if abs(self.get_f_medium_point()) < self.epsilon:
                finished_by_image = True

        if finished_by_image:
            print("Finished by image")
        else:
            print("Finished by domain")

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

    def show_final_table(self):
        tableHeader = ["n", "a", "b", "pm", "f(pm)"]
        tableContent = [
            [index for index, value in enumerate(self.a)],
            self.a,
            self.b,
            [*self.pm],
            [*self.fpm],
        ]

        transposed_table = list(zip(*tableContent))

        fig, ax = plt.subplots()

        # Create the table plot
        table = ax.table(cellText=transposed_table, loc="center", colLabels=tableHeader)

        # Hide axes
        ax.axis("off")

        # Adjust layout
        plt.subplots_adjust(left=0.2, bottom=0.2)

        # Show the plot
        plt.show()


if __name__ == "__main__":
    bissecao = Bissecao(lambda x: x**2 - 2, 0, 10, 1e-6)
    bissecao.estimate_iterations()
    start_time = time.time()
    result = bissecao.calculate_root()
    finish_time = time.time()

    print(
        f"Resultado: {result} \nTempo da resolução: \
          {finish_time - start_time} seconds"
    )

    bissecao.show_final_table()

    bissecao.show_method_progression()

    # ex2 = lambda x: x**3 + x - 3
    # ex2_plotter = Plotter(ex2)

    # ex2_plotter.plot_functions(-10, 10)

    # bissecao2 = Bissecao(ex2, -10, 10)
    # bissecao2.calculate_root()
    # bissecao2.show_method_progression()
