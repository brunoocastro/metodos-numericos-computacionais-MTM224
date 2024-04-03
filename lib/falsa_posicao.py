import time

from lib.bissecao import Bissecao


class FalsaPosicao(Bissecao):
    name = "Falsa posição"

    def get_medium_point(self):
        nominator = (self.a[-1] * self.f(self.b[-1])) - (
            self.b[-1] * self.f(self.a[-1])
        )
        denominator = self.f(self.b[-1]) - self.f(self.a[-1])

        return nominator / denominator

    def estimate_iterations(self):
        raise Exception("Nesse método não é possível determinar o numero de iterações")


if __name__ == "__main__":
    falsa_posicao = FalsaPosicao(lambda x: x**2 - 2, 1.3, 10, 1e-6)
    start_time = time.time()
    result = falsa_posicao.calculate_root()
    finish_time = time.time()

    print(
        f"Resultado: {result} \nTempo da resolução: \
          {finish_time - start_time} seconds"
    )

    falsa_posicao.show_final_table()

    falsa_posicao.show_method_progression()
