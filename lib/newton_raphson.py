from matplotlib import pyplot as plt
from lib.zeros_funcoes import ZerosFuncoes


class NewtonRaphson(ZerosFuncoes):
    name = "Newton Raphson"
    domain_error = ["-"]
    image_error = ["-"]

    def __init__(self, f, fprime, x0, error=0.0001, max_iterations=1000):
        self.f = f
        self.fprime = fprime
        self.domain = [x0]
        self.image = [f(x0)]
        self.prime_image = [fprime(x0)]
        self.epsilon = error
        self.max_iterations = max_iterations

    def get_new_point(self):
        next_x = self.domain[-1] - (
            self.f(self.domain[-1]) / self.fprime(self.domain[-1])
        )
        return next_x

    def get_domain_error(self):
        return abs(self.domain[-1] - self.domain[-2]) / abs(self.domain[-1])

    def step(self):
        x_plus_1 = self.get_new_point()
        self.domain.append(x_plus_1)

        y_plus_1 = self.f(x_plus_1)
        self.image.append(y_plus_1)

        yprime_plus_1 = self.fprime(x_plus_1)
        self.prime_image.append(yprime_plus_1)

        self.domain_error.append(self.get_domain_error())
        self.image_error.append(self.get_image_error())
        return x_plus_1, y_plus_1

    def calculate_root(self):
        iteration = 0

        while iteration < self.max_iterations:
            iteration += 1
            self.step()

            if self.domain_error[-1] < self.epsilon:
                self.finished_by_domain = True
                print("A raiz foi encontrada pelo domínio.")
                break

            if self.image_error[-1] < self.epsilon:
                self.finished_by_image = True
                print("A raiz foi encontrada pela imagem.")
                break

            ##if iteration % 10 == 0:
            print(f"Iteração {iteration}: {self.domain[-1]}")
            print(f"Erro pela imagem: {self.get_image_error()}")
            print(f"Erro pelo domínio: {self.get_domain_error()}\n")

        print(
            f"Método finalizado {'pela imagem' if self.finished_by_image else 'pelo dominio'} na iteração {iteration}."
        )
        print(f"Raiz (pm): {self.get_new_point()} e F(pm): {self.get_f_new_point()}")

    def show_final_table(self):
        tableHeader = ["n", "x", "f(x)", "f'(x)", "Erro domínio", "Erro imagem"]
        tableContent = [
            [
                "Intervalo inicial" if index == 0 else index
                for index, value in enumerate(self.domain)
            ],
            self.domain,
            self.image,
            self.prime_image,
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
