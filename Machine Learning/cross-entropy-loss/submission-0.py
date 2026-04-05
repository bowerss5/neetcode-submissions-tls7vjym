import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        sum = pi = yi = 0
        for i in range(len(y_true)):
            pi = y_pred[i]
            pi += 10 ** -7
            yi = y_true[i]

            sum += (yi * np.log(pi) + ((1- yi) * np.log(1 - pi)))

        return round((-1 / len(y_true)) * sum, 4)
    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        sum = 0

        for i in range(len(y_true)):
            for c in range(len(y_true[0])):
                sum += y_true[i][c] * np.log(y_pred[i][c])

        return round((-1 / len(y_true)) * sum, 4)
