import numpy as np


class MetodoEliminacaoGauss:
    def __init__(self, matrixA, vectorB):
        self.matrixA = np.array(matrixA, dtype=float)
        self.vectorB = np.array(vectorB, dtype=float).reshape(-1, 1)

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

    def handlePivot(self, i, j):
        # pivotValue = self.solutionMatrix[j][j]

        # if pivotValue != 0:
        #     return

        # print(f"Pivot is equals ZERO in ({j},{j})")

        higher_pos = (j, j)
        higher_value = 0

        for row_index in range(j, self.solutionMatrix.shape[0]):
            if abs(self.solutionMatrix[row_index, j]) > abs(higher_value):
                higher_pos = (row_index, j)
                higher_value = self.solutionMatrix[row_index, j]

        if higher_value == 0:
            raise Exception("No pivot found. Determinante NULO")

        # print("\nChanging rows:")
        # print(f"Higher value in column j={j} is {higher_value} in {higher_pos}")
        # print(f"Changing Row {i} with Row {j}\n")

        # print(f"Solution matrix pre changes:\n{self.solutionMatrix}")

        aux_row = self.solutionMatrix[higher_pos[0]].copy()
        # print(f"Initial row on pos i={j}: {self.solutionMatrix[j]}")
        # print(f"New row on pos i={j}:", aux_row)
        self.solutionMatrix[higher_pos[0]] = self.solutionMatrix[j]
        self.solutionMatrix[j] = aux_row
        print(f"\nSolution matrix POS PIVOT CHANGES:\n{self.solutionMatrix}\n")

    def findTriangular(self):
        self.solutionMatrix = np.array(self.augmentedMatrix.copy())
        for j in range(
            0, self.n
        ):  # o valor final é exclusivo, ou seja, vai executar de 0 a n-1
            for i in range(
                j + 1, self.n + 1
            ):  # o valor final é exclusivo, ou seja, vai executar de 0 a n
                self.handlePivot(i, j)
                factor = self.solutionMatrix[i][j] / self.solutionMatrix[j][j]
                print(f"Factor in [{i},{j}]: {factor}")
                print("Linha i:", self.solutionMatrix[i])
                print("Linha j:", self.solutionMatrix[j])
                self.solutionMatrix[i] = (
                    self.solutionMatrix[i] - factor * self.solutionMatrix[j]
                )
                print("Final:", self.solutionMatrix[i])
                print(f"Solution matrix on [{i},{j}]: \n", self.solutionMatrix, "\n")

        print("Solution Matrix:")
        print(self.solutionMatrix)
        self.AUpper = self.solutionMatrix[:, :-1]
        self.BUpper = self.solutionMatrix[:, -1:]
        print("AUpper:")
        print(self.AUpper)
        print("BUpper:")
        print(self.BUpper)

        self.solutionMatrix = np.where(
            np.abs(self.solutionMatrix) < 1e-4, 0, self.solutionMatrix
        )
        self.AUpper = np.where(np.abs(self.AUpper) < 1e-4, 0, self.AUpper)
        self.BUpper = np.where(np.abs(self.BUpper) < 1e-4, 0, self.BUpper)

        return self.solutionMatrix, self.AUpper, self.BUpper


if __name__ == "__main__":
    matrixA = [[2, 2, 1, 1], [1, -1, 2, -1], [3, 2, -3, -2], [4, 3, 2, 1]]
    vectorB = [7, 1, 4, 12]

    gauss = MetodoEliminacaoGauss(matrixA, vectorB)
    gauss.printMatrix()

    gauss.findTriangular()
