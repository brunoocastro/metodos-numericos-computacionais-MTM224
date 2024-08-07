import time
import numpy as np

from matplotlib import pyplot as plt

from lib.zeros_funcoes.zeros_funcoes import ZerosFuncoes


class Bissecao(ZerosFuncoes):
    name = "Método da Bisseção"

    def __init__(self, f, a, b, error=0.0001):
        self.a = [a]
        self.b = [b]
        self.pm = ["-"]
        self.f = f
        self.fpm = ["-"]
        self.epsilon = error

        if (self.f(self.b[-1]) * self.f(self.a[-1])) > 0:
            raise Exception(
                f"O intervalo [{self.a[-1]},{self.b[-1]}] não é valido pois\
                      não há garantia de existência de raiz"
            )

    def get_domain_error(self):
        return abs(self.b[-1] - self.a[-1])

    def calculate_root(self):
        while not self.finished_by_image and not self.finished_by_domain:
            self.step()

            if self.get_domain_error() < self.epsilon:
                self.finished_by_domain = True

            if self.get_image_error() < self.epsilon:
                self.finished_by_image = True

        self.step()

        print(
            f"Método finalizado {'pela imagem' if self.finished_by_image else 'pelo dominio'}."
        )
        print(f"Raiz (pm): {self.get_new_point()} e F(pm): {self.get_f_new_point()}")

        return self.get_new_point()

    @staticmethod
    def has_solution(func, step=0.005):
        random_a = 0
        random_b = 1

        time_init = time.time()

        # pesquisar - método de busca incremental
        while func(random_a) * func(random_b) > 0:
            random_a -= 1
            random_b += 1

        lower_interval = random_a
        higher_interval = random_b

        while func(higher_interval) * func(lower_interval) < 0:
            lower_interval += step
            higher_interval -= step

        time_end = time.time()

        print(
            "Tempo de execução (encontrar intervalo com raiz): ",
            time_end - time_init,
            "s",
        )

        return lower_interval, higher_interval

    def estimate_iterations(self):
        startInterval = self.a[0]
        finishInterval = self.b[0]
        print(f"Intervalo inicial: [{startInterval},{finishInterval}]")

        higherThan = (
            np.log(finishInterval - startInterval) - np.log(self.epsilon)
        ) / np.log(2)

        N = int(np.ceil(higherThan))

        print(f"O número de iterações N é de {N}")

        return N

    def get_new_point(self):
        return (self.a[-1] + self.b[-1]) / 2

    def step(self):
        pm = self.get_new_point()
        self.pm.append(pm)

        fpm = self.get_f_new_point()
        self.fpm.append(fpm)
        if fpm * self.f(self.a[-1]) < 0:
            self.a.append(self.a[-1])
            self.b.append(pm)
        else:
            self.a.append(pm)
            self.b.append(self.b[-1])

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
        ax.set_title(f"Progressão do {self.name}")
        ax.grid(True)
        # plt.savefig("bisection_progression.png")
        plt.show()

    def show_final_table(self):
        tableHeader = ["n", "a", "b", "pm", "f(pm)"]
        tableContent = [
            [
                "Intervalo inicial" if index == 0 else index
                for index, value in enumerate(self.a)
            ],
            self.a,
            self.b,
            [*self.pm],
            [*self.fpm],
        ]

        transposed_table = list(zip(*tableContent))

        fig, ax = plt.subplots()

        # adjust table text size to be visible
        ax.set_title(f"{self.name} - Tabela de iterações", fontsize=20)

        # Create the table plot
        table = ax.table(cellText=transposed_table, loc="center", colLabels=tableHeader)

        # adjust cell text size to be visible
        table.set_fontsize(16)
        table.scale(2, 2)  # may help

        # Hide axes
        ax.axis("off")

        # Adjust layout
        plt.subplots_adjust(left=0.2, bottom=0.2)

        # Show the plot
        plt.show()


if __name__ == "__main__":
    bissecao = Bissecao(lambda x: x**2 - 2, 0, 10, 1e-14)
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
