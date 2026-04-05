class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1] * (n + 1)
        i = 2
        if n > 2:
            stairs[2] = 2
        while i <= n:
            print(i)
            stairs[i] = stairs[i - 1] + stairs[i - 2]
            i += 1


        return stairs[n]
