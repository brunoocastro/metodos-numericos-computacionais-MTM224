import numpy as np
import matplotlib.pyplot as plt

from lib.sis_eq_lin.met_eliminacao_gauss import MetodoEliminacaoGauss


class MetodoInterpolacaoPolinomial:
    def __init__(self, X, Y):
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.degree = len(X) - 1
        self.matrixA = self.createMatrix(self.X)
        self.coefficients = None

    def createMatrix(self, X):
        """Create the matrix for polynomial interpolation"""
        n = len(X)
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i, j] = X[i] ** j
        return A

    def solveUpperTriangular(AUpper, BUpper):
        """Solve an upper triangular system of equations"""
        A = AUpper
        b = BUpper
        n = len(b)
        x = np.zeros_like(b)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i+1:], x[i + 1 :])) / A[i, i]
        return x.flatten()

    def fit(self):
        """Fit the polynomial to the data using Gaussian Elimination"""
        A = self.matrixA
        b = self.Y
        gauss = MetodoEliminacaoGauss(A, b)
        solutionMatrix, AUpper, BUpper, factorMatrix = gauss.findTriangular()
        self.solveUpperTriangular(AUpper, BUpper)

    def predict(self, X):
        """Predict values using the interpolated polynomial"""
        n = len(self.coefficients)
        Y = np.zeros_like(X, dtype=float)
        for i in range(n):
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
