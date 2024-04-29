import numpy as np


class ResSisLin:
    def __init__(self, matrixA: np.ndarray, vectorB: np.ndarray):
        self.matrixA = matrixA
        self.vectorB = vectorB

        # Verifica se a matriz é quadrada e o vetor solução tem o mesmo tamanho
        print(self.vectorB.shape, self.matrixA.shape)
        if self.vectorB.shape[0] != self.matrixA.shape[0]:
            raise Exception("Vetor solução tem dimensão diferente ")

        # Verifica se a matriz é triangular superior ou inferior
        isValid, self.isUpper, self.isLower = self.isTriangular(self.matrixA)

        if not isValid:
            raise Exception("Matriz não é triangular")

        # Print received Matrix A and Vector B
        print("Received Matrix A:")
        print(self.matrixA)
        print("Received Vector B:")
        print(self.vectorB)

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

        sisShape = self.matrixA.shape[0]

        variationInterval = range(sisShape - 1, 0)
        if self.isLower:
            variationInterval = range(1, sisShape)

        print(f"Variation interval for I: {variationInterval} with shape {sisShape}")

        solution = np.zeros((sisShape))
        solution[-1] = self.vectorB[-1] / self.matrixA[-1][-1]

        print(f"Initial Solution: {solution}")
        for i in variationInterval:
            sum = 0
            print(f"i: {i}")
            for j in range(i, sisShape):
                print(f"i: {i}, j: {j}, sum: {sum}")
                sum += self.matrixA[i][j] * self.matrixA[j][i]  # Corrigir

            solution[i] = self.getXn((self.vectorB[i] - sum), self.matrixA[i][i])

        print(f"Solution: {solution}")
        return solution


if __name__ == "__main__":
    triangularA = np.array([[3, 2, 4], [0, 1 / 3, 2 / 3], [0, 0, -8]])
    vetorTriangularB = np.array([1, 5 / 3, 0])

    res = ResSisLin(triangularA, vetorTriangularB)
    solution = res.findSolution()

    print(solution)
