import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        result = z[:]

        for i in range(len(z)):
            result[i] = round(1 / (1 + math.exp(-1 * z[i])), 5)

        return result

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        result = z[:]

        for i in range(len(z)):
            result[i] = max(0, z[i])

        return result

