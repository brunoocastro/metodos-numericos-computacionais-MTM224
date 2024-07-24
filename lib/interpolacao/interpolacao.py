import numpy as np
import matplotlib.pyplot as plt

from lib.sis_eq_lin.met_eliminacao_gauss import MetodoEliminacaoGauss
from lib.sis_eq_lin.res_sistemas_triang import ResSisLin


class MetodoInterpolacaoPolinomial:
    def __init__(self, X, Y):
        # 1) Obter Inputs
        self.X = np.array(X)
        self.Y = np.array(Y)

        # 1.1) Definir grau
        self.degree = len(X) - 1

        # 2) Gerar matriz A
        self.matrixA = self.createMatrix(self.X)
        # 3) Gerar vetor B
        self.vectorB = self.Y

        self.coefficients = None

    def createMatrix(self, X):
        """Create the matrix for polynomial interpolation"""
        n = len(X)
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = X[i] ** j
        return A

    def fitPolynomial(self):
        gauss = MetodoEliminacaoGauss(self.matrixA, self.vectorB)
        _, AUpper, BUpper, _ = gauss.findTriangular()

        sisLin = ResSisLin(AUpper, BUpper)

        sol = sisLin.findSolution()

        # Atualizando coeficientes com o vetor inverso da resposta
        self.coefficients = (sol)

        print("Coeficientes do Polinômio:", self.coefficients)

    def predict(self, X):
        """Predict values using the interpolated polynomial"""
        n = len(self.coefficients)
        Y = np.zeros_like(X, dtype=float)

        # Para cada coeficiente do array
        for i in range(n):
            # Y = somatório do coeficiente * X elevado i
            Y += self.coefficients[i] * X**i
        return Y

    def plotDataAndFit(self):
        """Plot the original data and the polynomial fit"""
        plt.scatter(self.X, self.Y, label="Data", color="blue")
        X_fit = np.linspace(min(self.X), max(self.X), 1000)
        Y_fit = self.predict(X_fit)
        plt.plot(X_fit, Y_fit, label="Polynomial Interpolator", color="red")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()
