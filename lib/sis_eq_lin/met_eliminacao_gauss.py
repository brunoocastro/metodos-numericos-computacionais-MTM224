class MetodoEliminacaoGauss:
    def __init__(self, matrixA, vectorB):
        self.matrixA = matrixA
        self.vectorB = vectorB

        self.augmentedMatrix = self.matrixA.copy()
        self.augmentedMatrix.append(self.vectorB)

        self.n = len(self.matrixA)

    def printMatrix(self):
        print("Received Matrix A:")
        print(self.matrixA)
        print("Received Vector B:")
        print(self.vectorB)

    def findUpper(self):
        self.solutionMatrix = self.augmentedMatrix.copy()
        for j in range(self.n - 1):
            for i in range(j + 1, self.n):
                factor = self.solutionMatrix[i][j] / self.solutionMatrix[j][j]
                self.solutionMatrix[i] = (
                    self.solutionMatrix[i] - factor * self.solutionMatrix[j]
                )

        print("Solution Matrix:")
        print(self.solutionMatrix)
        AUpper = self.solutionMatrix[: self.n]
        BUpper = self.solutionMatrix[self.n :]
        print("AUpper:")
        print(AUpper)
        print("BUpper:")
        print(BUpper)
        return self.solutionMatrix, AUpper, BUpper
