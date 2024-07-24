import numpy as np
import matplotlib.pyplot as plt

from lib.sis_eq_lin.met_eliminacao_gauss import MetodoEliminacaoGauss
from lib.sis_eq_lin.res_sistemas_triang import ResSisLin


class MetodoMinimosQuadrados:
    def __init__(self, X, Y, degree):
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.degree = degree

        if self.degree >= len(self.X):
            raise ValueError(
                f"O grau do polinômio deve ser no máximo igual (N - 1) para X com tamanho N.\nNeste caso o grau máximo é {len(self.X) - 1}"  # noqa
            )

        self.matrixA = self.createMatrix(self.X, self.degree)
        print(f"Matriz A: \n{self.matrixA}")
        self.coefficients = None

    def createMatrix(self, X, degree):
        n = len(X)
        A = np.zeros((n, degree + 1))
        for i in range(degree + 1):
            A[:, i] = X**i
        print("A")
        return A

    def findCoefficients(self):
        A = self.matrixA
        b = self.Y

        # ! Validar esse processo:
        # A.T -> Transposta da matriz
        # @ faz a multiplicação da matriz resultante pela matriz B
        # ! Onde B é o vetor coluna de Y
        # ! Onde A.T @ A é a matriz quadrada de coeficientes
        # ! Onde A.T @ b é o vetor coluna de X
        AT_A = A.T @ A  # Compute A^T * A
        AT_b = A.T @ b  # Compute A^T * b

        gauss = MetodoEliminacaoGauss(AT_A, AT_b)
        _, A_upper, B_upper, _ = gauss.findTriangular()

        sis_lin = ResSisLin(A_upper, B_upper)
        self.coefficients = sis_lin.findSolution()

    def predict(self, X):
        """Predict values using the fitted model"""
        A = self.createMatrix(X, self.degree)
        return A @ self.coefficients

    def meanSquaredError(self):
        """Calculate the mean squared error of the model"""
        predictions = self.predict(self.X)
        mse = np.mean((self.Y - predictions) ** 2)
        return mse

    def rSquared(self):
        """Calculate the R^2 value of the model"""
        predictions = self.predict(self.X)  #
        ss_total = np.sum((self.Y - np.mean(self.Y)) ** 2)
        ss_residual = np.sum((self.Y - predictions) ** 2)
        r2 = 1 - (ss_residual / ss_total)
        return r2

    def printCoefficients(self):
        """Print the coefficients of the model"""
        print("Coefficients of the model:\n", self.coefficients)

    def plotDataAndFit(self):
        """Plot the original data and the polynomial fit"""
        plt.scatter(self.X, self.Y, label="Data", color="blue")

        X_fit = np.linspace(min(self.X), max(self.X), 1000)
        Y_fit = self.predict(X_fit)

        plt.plot(
            X_fit, Y_fit, label=f"Polynomial Fit (degree={self.degree})", color="red"
        )
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()

        plt.show()
