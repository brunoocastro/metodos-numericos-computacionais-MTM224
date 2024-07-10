import numpy as np
import matplotlib.pyplot as plt

from lib.sis_eq_lin.met_eliminacao_gauss import MetodoEliminacaoGauss


class MetodoMinimosQuadrados:
    def __init__(self, X, Y, degree):
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.degree = degree
        self.designMatrix = self.createDesignMatrix(self.X, self.degree)
        self.coefficients = None

    def createDesignMatrix(self, X, degree):
        """Create a design matrix for polynomial fitting"""
        n = len(X)
        A = np.zeros((n, degree + 1))
        for i in range(degree + 1):
            A[:, i] = X**i
        return A

    def fit(self):
        """Fit the model to the data using the least squares method with Gauss Elimination"""
        A = self.designMatrix
        b = self.Y
        AT_A = A.T @ A
        AT_b = A.T @ b
        gauss = MetodoEliminacaoGauss(AT_A, AT_b)
        _, A_upper, B_upper, _ = gauss.findTriangular()
        self.coefficients = self.solveUpperTriangular(A_upper, B_upper)

    def solveUpperTriangular(self, A, b):
        """Solve an upper triangular system of equations"""
        n = len(b)
        x = np.zeros_like(b)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1 :], x[i + 1 :])) / A[i, i]
        return x

    def predict(self, X):
        """Predict values using the fitted model"""
        A = self.createDesignMatrix(X, self.degree)
        return A @ self.coefficients

    def meanSquaredError(self):
        """Calculate the mean squared error of the model"""
        predictions = self.predict(self.X)
        mse = np.mean((self.Y - predictions) ** 2)
        return mse

    def rSquared(self):
        """Calculate the R^2 value of the model"""
        predictions = self.predict(self.X)
        ss_total = np.sum((self.Y - np.mean(self.Y)) ** 2)
        ss_residual = np.sum((self.Y - predictions) ** 2)
        r2 = 1 - (ss_residual / ss_total)
        return r2

    def printCoefficients(self):
        """Print the coefficients of the model"""
        print("Coefficients of the model:", self.coefficients)

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
