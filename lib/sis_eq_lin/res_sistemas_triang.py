import numpy as np


class ResSisLin:
    def __init__(self, sisTriangular: np.ndarray, vetorSolucao: np.ndarray):
        self.sisLin = sisTriangular
        self.vecSolucao = vetorSolucao

        # Verifica se a matriz é quadrada e o vetor solução tem o mesmo tamanho
        print(self.vecSolucao.shape, self.sisLin.shape)
        if self.vecSolucao.shape[0] != self.sisLin.shape[0]:
            raise Exception("Vetor solução tem dimensão diferente ")

        # Verifica se a matriz é triangular superior ou inferior
        isValid, self.isUpper, self.isLower = self.isTriangular(sisTriangular)

        if not isValid:
            raise Exception("Matriz não é triangular")

    @staticmethod
    # Describing method
    def isTriangular(sisTriangular):
        """
        Verifica se a matriz é triangular superior ou inferior
        Retorna o seguinte em boolean: [é triangular, é superior, é inferior]
        :param sisTriangular: matriz triangular
        :return: boolean, boolean, boolean
        """
        isUpper = True
        isLower = True

        shape = sisTriangular.shape
        # Verifica se a matriz é superior
        for i in range(shape[0]):
            for j in range(shape[1]):
                if i > j and sisTriangular[i][j] != 0:
                    isUpper = False

        # Verifica se a matriz é inferior
        for i in range(shape[0]):
            for j in range(shape[1]):
                if i < j and sisTriangular[i][j] != 0:
                    isLower = False

        if isUpper:
            print("Matriz é triangular superior")

        if isLower:
            print("Matriz é triangular inferior")

        return isUpper or isLower, isUpper, isLower

    @staticmethod
    def getXn(bn, ann):
        return bn / ann

    def findSolution(self):
        """
        Encontra a solução do sistema linear
        :return: matriz com a solução
        """

        sisShape = self.sisLin.shape[0]

        variationInterval = range(sisShape - 1, 1)
        if self.isLower:
            variationInterval = range(1, sisShape)

        print(f"Variation interval for I: {variationInterval}, {sisShape}")

        solution = np.zeros(sisShape)
        solution[-1] = self.vecSolucao[-1] / self.sisLin[-1][-1]

        print(f"Initial Solution: {solution}")
        for i in variationInterval:
            sum = 0
            print(f"i: {i}")
            for j in range(i, sisShape):
                print(f"i: {i}, j: {j}, sum: {sum}")
                sum += self.sisLin[i][j] * self.sisLin[j][i]  # Corrigir

            solution[i] = self.getXn((self.vecSolucao[i] - sum), self.sisLin[i][i])

        print(f"Solution: {solution}")
        return solution
