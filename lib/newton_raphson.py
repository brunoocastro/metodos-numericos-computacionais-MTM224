import time

from lib.bissecao import Bissecao
from lib.zeros_funcoes import ZerosFuncoes


class NewtonRaphson(ZerosFuncoes):
    name = "Newton Raphson"

    def __init__(self, f, fprime, x0, error=0.0001, max_iterations=1000):
        self.f = f
        self.fprime = fprime
        self.x0 = x0
        self.epsilon = error
        self.max_iterations = max_iterations

    def get_new_point(self):
        

        return nominator / denominator

    def estimate_iterations(self):
        raise Exception("Nesse método não é possível determinar o numero de iterações")


if __name__ == "__main__":
    falsa_posicao = NewtonRaphson(lambda x: x**2 - 2, 1.3, 10, 1e-6)
    start_time = time.time()
    result = falsa_posicao.calculate_root()
    finish_time = time.time()

    print(
        f"Resultado: {result} \nTempo da resolução: \
          {finish_time - start_time} seconds"
    )

    falsa_posicao.show_final_table()

    falsa_posicao.show_method_progression()
