import random
import time

from matplotlib import pyplot as plt

from Plotter import Plotter


class Bissecao:
    def __init__(self, a, b, f, error=0.0001):
        self.a = [a]
        self.b = [b]
        self.pm = ['-']
        self.f = f
        self.fpm = ['-']
        self.max_error = error

    @staticmethod
    def has_solution(self, function):
        random_a = random.random() * 10

        lower_interval = random_a

        while function(lower_interval) < 0:
            lower_interval += random_a

        return self.f(self.a[0]) * self.f(self.b[0]) < 0

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
            
            if abs(self.b[-1] - self.a[-1]) < self.max_error:
                finished_by_domain = True
            
            if abs(self.get_f_medium_point()) < self.max_error:
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
        tableHeader = ["a", "b", "pm", "f(pm)"]
        tableContent = [self.a, self.b, ['-', *self.pm], ['-', *self.fpm]]

        transposed_table = list(zip(*tableContent))

        fig, ax = plt.subplots()

        # Create the table plot
        table = ax.table(cellText=transposed_table, loc='center', colLabels=tableHeader)

        # Hide axes
        ax.axis('off')

        # Adjust layout
        plt.subplots_adjust(left=0.2, bottom=0.2)

        # Show the plot
        plt.show()

        


if __name__ == "__main__":
    bissecao = Bissecao(0, 10, lambda x: x**2 - 2, 1e-6)
    start_time = time.time()
    result = bissecao.calculate_root()
    finish_time = time.time()

    print(
        f"Resultado: {result} \nTempo da resolução: \
          {finish_time - start_time} seconds"
    )

    bissecao.show_final_table()

    bissecao.show_method_progression()

    ex2 = lambda x: x**3 + x - 3
    ex2_plotter = Plotter(ex2)

    ex2_plotter.plot_functions(-10,10)

    bissecao2 = Bissecao(-10, 10, ex2)
    bissecao2.calculate_root()
    bissecao2.show_method_progression()
