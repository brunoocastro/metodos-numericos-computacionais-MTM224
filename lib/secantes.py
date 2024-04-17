from matplotlib import pyplot as plt
from lib.newton_raphson import NewtonRaphson


class Secantes(NewtonRaphson):
    name = "Secantes"
    domain_error = ["-"]
    image_error = ["-"]

    def __init__(self, f, x0, x1, error=0.0001, max_iterations=1000):
        self.f = f
        self.domain = [x0, x1]
        self.image = [f(x0), f(x1)]
        self.epsilon = error
        self.max_iterations = max_iterations

    def get_new_point(self):
        next_x = self.domain[-1] - (
            (self.f(self.domain[-1]) * (self.domain[-1] - self.domain[-2]))
            / (self.f(self.domain[-1]) - self.f(self.domain[-2]))
        )
        return next_x

    def step(self):
        x_curr = self.domain[-1]
        x_plus_1 = self.get_new_point()
        self.domain.append(x_plus_1)

        # y_current = self.f(x_curr)
        # self.y.append(y_current)

        y_plus_1 = self.f(x_plus_1)
        self.image.append(y_plus_1)

        self.domain_error.append(self.get_domain_error())
        self.image_error.append(self.get_image_error())
        return x_curr, x_plus_1

    def show_final_table(self):
        tableHeader = ["n", "x", "f(x)", "Erro domínio", "Erro imagem"]
        tableContent = [
            [
                "Intervalo inicial" if index == 0 else index
                for index, value in enumerate(self.domain)
            ],
            self.domain,
            self.image,
            self.domain_error,
            self.image_error,
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
