import numpy as np


class MetodoEliminacaoGauss:
    def __init__(self, matrixA, vectorB):
        self.matrixA = np.array(matrixA)
        self.vectorB = np.array(vectorB).reshape(-1, 1)

        self.augmentedMatrix = self.matrixA.copy()
        self.augmentedMatrix = np.append(self.augmentedMatrix, self.vectorB, axis=1)

        self.n = self.matrixA.shape[0] - 1

    def printMatrix(self):
        print(f"Received Matrix A with shape {self.matrixA.shape}:")
        print(self.matrixA)
        print(f"Received Vector B with shape {self.vectorB.shape}:")
        print(self.vectorB)

        print("---------------")
        print("Augmented Matrix:")
        print(self.augmentedMatrix)

    def findTriangular(self):
        self.solutionMatrix = np.array(self.augmentedMatrix.copy())
        for j in range(
            0, self.n
        ):  # o valor final é exclusivo, ou seja, vai executar de 0 a n-1
            for i in range(j + 1, self.n + 1):
                factor = self.solutionMatrix[i][j] / self.solutionMatrix[j][j]
                print(f"Factor in [{i},{j}]: {factor}")
                self.solutionMatrix[i] = (
                    self.solutionMatrix[i] - factor * self.solutionMatrix[j]
                )

        print("Solution Matrix:")
        print(self.solutionMatrix)
        AUpper = self.solutionMatrix[:, :-1]
        BUpper = self.solutionMatrix[:, -1:]
        print("AUpper:")
        print(AUpper)
        print("BUpper:")
        print(BUpper)
        return self.solutionMatrix, AUpper, BUpper


if __name__ == "__main__":
    matrixA = [[2, 2, 1, 1], [1, -1, 2, -1], [3, 2, -3, -2], [4, 3, 2, 1]]
    vectorB = [7, 1, 4, 12]

    gauss = MetodoEliminacaoGauss(matrixA, vectorB)
    gauss.printMatrix()

    gauss.findTriangular()
