import numpy as np
from lib.sis_eq_lin.met_eliminacao_gauss import MetodoEliminacaoGauss
from lib.sis_eq_lin.res_sistemas_triang import ResSisLin


class SolucaoSistemasLineares:
    def __init__(self, matrixA, vectorB)
        self.matrixA = np.array(matrixA, dtype=float)
        self.vectorB = np.array(vectorB, dtype=float)
        self.method = MetodoEliminacaoGauss

    def findTriangular(self):
        return self.method.findTriangular(self.matrixA, self.vectorB)

    def findSolution(self, TriangA, TriangB):
        sol = ResSisLin(TriangA, TriangB)
        finalSolution = sol.findSolution()
        return finalSolution


if __name__ == "__main__":
    matrixA = [[2, 2, 1, 1], [1, -1, 2, -1], [3, 2, -3, -2], [4, 3, 2, 1]]
    vectorB = [7, 1, 4, 12]

    sol = SolucaoSistemasLineares(matrixA, vectorB)
    augmented, matrixA, vectorB = sol.findTriangular()

    solution = sol.findSolution()
