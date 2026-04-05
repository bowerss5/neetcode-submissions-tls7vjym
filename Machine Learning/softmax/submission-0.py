import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        result = z[:]
        maxE = max(z)

        sum = 0

        for num in z:
            sum += math.exp(num - maxE)

        for i in range(len(result)):
            result[i] = round(math.exp(z[i] - maxE) / sum, 4)


        return result
