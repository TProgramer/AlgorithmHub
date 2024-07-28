class Solution:
    def tribonacci(self, n: int) -> int:
        # define array to memorize previous result
        dp = [0, 1, 1] + [0] * (n - 2)

        # loop to compute value of n in tribonacci tree
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        # return N-th tribonacci number
        return dp[n]