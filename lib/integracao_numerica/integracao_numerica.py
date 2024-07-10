import math


def trapezoid_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    return integral * h


def simpson_rule(f, a, b, n):
    h = (b - a) / n
    if n % 2 == 0:
        raise ValueError("n must be odd for Simpson's rule")
    integral = f(a) + f(b)
    for i in range(1, n // 2):
        x = a + (2 * i - 1) * h
        integral += 2 * f(x)
    for i in range(1, n // 2 + 1):
        x = a + 2 * i * h
        integral += 4 * f(x)
    return integral * h / 3


def f(x):
    # Example function: x^2 + sin(x)
    return x**2 + math.sin(x)


# Test the functions
a = 0.0
b = math.pi
n = 1000

print("Trapezoidal Rule:")
print(trapezoid_rule(f, a, b, n))

print("\nSimpson's Rule:")
print(simpson_rule(f, a, b, n))


class IntegracaoNumerica:
    def __init__(self, f, n, a, b) -> None:
        self.f = f
        self.n = n
        self.a = a
        self.b = b
