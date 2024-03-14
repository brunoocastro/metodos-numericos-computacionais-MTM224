import time


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
            self.b.append(self.get_medium_point())
        else:
            self.a.append(self.get_medium_point())

    def calculate_root(self):
        while abs(self.b[-1] - self.a[-1]) > self.max_error:
            self.calculate_interval()
        return self.get_medium_point()


if __name__ == "__main__":
    bissecao = Bissecao(0, 2, lambda x: x**2 - 2, 1e-10)
    start_time = time.time()
    result = bissecao.calculate_root()
    finish_time = time.time()
    print(f"Resultado: {result} \nTempo da resolução: {finish_time - start_time} seconds")
