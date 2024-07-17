import numpy as np


class MetodoIterativoGaussJacobi:
    def __init__(self, A, b, tolerance=1e-10, max_iterations=1000):
        """Initialize with matrix A, vector b, tolerance and maximum iterations"""
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
        """Check for convergence"""
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
                return False

        print("The matrix C is convergent.")
        return True

    def verifyStopCriteria(self):
        """Check for stop criteria"""
        self.iterations = self.iterations + 1
        print("Iteration:", self.iterations)

        if self.iterations > self.max_iterations:
            print(f"Finish by finding maximum iterations - {self.iterations}")
            return True

        diff = abs(self.x[self.iterations] - self.x[self.iterations - 1]) / abs(
            self.x[self.iterations]
        )

        if self.tolerance > diff:
            print(f"Finish by finding tolerance - in {self.iterations} iterations")
            self.x = self.x_new.copy()
            return True

        return False

    def solve(self):
        """Solve the system using Gauss-Jacobi iterative method"""

        self.findCMatrix()

        converges = self.verifyConvergence()

        if not converges:
            raise ValueError("The matrix is not convergent.")

        n = len(self.b)
        x = np.zeros_like(self.b)  # Initial guess (zeros)
        x_new = np.zeros_like(x)

        for iteration in range(self.max_iterations):
            for i in range(n):
                s = sum(self.A[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (self.b[i] - s) / self.A[i][i]

            # Check for convergence

            if self.verifyStopCriteria():
                self.solution = x_new
                print(f"Converged in {iteration + 1} iterations.")
                return self.solution

            x = x_new.copy()

        print("Did not converge within the maximum number of iterations.")
        self.solution = x_new
        return self.solution


# Example usage:
if __name__ == "__main__":
    A = [[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]]
    b = [15, 10, 10, 10]
    gauss_jacobi = MetodoIterativoGaussJacobi(A, b)
    solution = gauss_jacobi.solve()
    print("Solution:", solution)
