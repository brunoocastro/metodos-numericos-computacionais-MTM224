import numpy as np
from lib.sis_eq_lin.met_eliminacao_gauss import MetodoEliminacaoGauss
from lib.sis_eq_lin.res_sistemas_triang import ResSisLin


class FatoracaoLU:
    def __init__(self, matrixA, vectorB) -> None:
        self.matrixA = np.array(matrixA, dtype=float)
        self.vectorB = np.array(vectorB, dtype=float)

    def findLU(self):
        GaussMethod = MetodoEliminacaoGauss(self.matrixA, self.vectorB)

        _, matrixU, _, matrixL = GaussMethod.findTriangular()

        self.matrixL = np.array(matrixL, dtype=float)
        self.matrixU = np.array(matrixU, dtype=float)

        print(f"Matrix L: \n{self.matrixL}")
        print(f"Matrix U: \n{self.matrixU}")

    def getY(self):
        sisLinY = ResSisLin(self.matrixL, self.vectorB)
        vectorY = sisLinY.findSolution()

        self.vectorY = np.array(vectorY, dtype=float)
        print(f"Vetor Y = {self.vectorY}")

    def getX(self):
        sisLinX = ResSisLin(self.matrixU, self.vectorY)
        vectorX = sisLinX.findSolution()

        self.vectorX = np.array(vectorX, dtype=float)
        print(f"Solução final: {self.vectorX}")

    def findSolution(self):
        self.findLU()
        self.getY()
        self.getX()

        return self.vectorX, self.vectorY
