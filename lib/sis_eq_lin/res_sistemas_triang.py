import numpy as np


class ResSisLin:
    def __init__(self, matrixA: np.ndarray, vectorB: np.ndarray):
        self.matrixA = np.array(matrixA, dtype=float)
        self.vectorB = np.array(vectorB, dtype=float)

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
        solution = np.zeros((sisShape))

        array_size = sisShape - 1

        # Variation interval for (n - 1) to 0 (-1 open on rage)
        if self.isUpper:
            variationIntervalI = range(array_size - 1, -1, -1)
            solution[-1] = self.vectorB[-1] / self.matrixA[-1][-1]

            def getJInterval(i):
                return range(i + 1, array_size + 1)

        if self.isLower:
            solution[0] = self.vectorB[0] / self.matrixA[0][0]
            variationIntervalI = range(1, array_size + 1)

            def getJInterval(i):
                return range(0, i + 1)

        print(
            f"Variation interval for I: {variationIntervalI}\
                  with shape (0,{array_size})"
        )
        print(f"Variation Interval for J: {getJInterval(0)}")

        print(f"Initial Solution: {solution}")

        for i in variationIntervalI:
            sum = 0
            print(f"i: {i}")
            for j in getJInterval(i):
                sum += self.matrixA[i][j] * solution[j]
                print(f"i: {i}, j: {j}, sum: {sum}")

            solution[i] = (self.vectorB[i] - sum) / self.matrixA[i][i]
            print(f"Solution:\n{solution}\n")

        solution = np.round(solution, 4)

        print(f"Solution: {solution}")
        return solution


if __name__ == "__main__":
    triangularA = np.array([[3, 2, 4], [0, 1 / 3, 2 / 3], [0, 0, -8]])
    vetorTriangularB = np.array([1, 5 / 3, 0])

    res = ResSisLin(triangularA, vetorTriangularB)
    solution = res.findSolution()

    print(solution)
