import numpy as np


class MetodoIterativoGaussJacobi:
    def __init__(self, A, b, tolerance=1e-10, max_iterations=1000):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.C = np.empty((len(self.b), len(self.b)))

        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.solution = None
        self.points = []
        self.iterations = 0

    def findCMatrix(self):
        n = len(self.b)
        self.g = np.empty(n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.C[i][j] = 0
                else:
                    self.C[i][j] = -self.A[i][j] / self.A[i][i]
            self.g[i] = self.b[i] / self.A[i, i]

        print("C Matrix:\n", self.C)
        print("G Vector:\n", self.g)

    def verifyConvergence(self):
        self.alfa = np.zeros_like(self.b)

        print("Alfa:", self.alfa)

        for i in range(len(self.A)):
            for j in range(len(self.A)):
                self.alfa[i] = self.alfa[i] + abs(self.C[i, j])

        print("Alfa dps de computar:", self.alfa)

        max_alfa = max(self.alfa)
        print("Max alfa:", max_alfa)

        if max_alfa >= 1:
            self.beta = np.zeros_like(self.b)
            for j in range(len(self.A)):
                for i in range(len(self.A)):
                    self.beta[i] = self.beta[i] + abs(self.C[i, j])

            max_beta = max(self.beta)

            if max_beta >= 1:
                print("The matrix C is not convergent.")

                return False

        print("The matrix C is convergent.")
        return True

    def verifyStopCriteria(self):
        self.iterations = self.iterations + 1
        print("\nIteracao:", self.iterations)

        if self.iterations > self.max_iterations:
            print(f"Finish by finding maximum iterations - {self.iterations}")
            return True

        diff = abs(max(self.x_new) - max(self.x)) / max(abs(self.x_new))

        print(
            f"Verificando criterio de parada:\nDiff: {diff} | Tolerance: {self.tolerance}"
        )

        if self.tolerance > diff:
            print(f"Finish by finding tolerance - in {self.iterations} iterations")
            self.x = self.x_new.copy()
            return True

        return False

    def solve(self):
        self.findCMatrix()

        converges = self.verifyConvergence()

        if not converges:
            raise ValueError("The matrix is not convergent.")

        self.n = len(self.b)
        self.x = np.zeros_like(self.b)  # Initial guess (zeros)
        self.x_new = np.zeros_like(self.x)

        for iteration in range(self.max_iterations):
            for i in range(self.n):
                total_sum = sum(
                    self.A[i][j] * self.x[j] for j in range(self.n) if j != i
                )
                self.x_new[i] = (self.b[i] - total_sum) / self.A[i][i]

            # Check for convergence

            if self.verifyStopCriteria():
                self.solution = self.x_new
                print(f"Converged in {iteration + 1} iterations.")
                return self.solution

            self.x = self.x_new.copy()

        print("Did not converge within the maximum number of iterations.")
        self.solution = self.x_new

        return self.solution


# Example usage:
if __name__ == "__main__":
    A = [[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]]
    b = [15, 10, 10, 10]
    gauss_jacobi = MetodoIterativoGaussJacobi(A, b)
    solution = gauss_jacobi.solve()
    print("Solution:", solution)
