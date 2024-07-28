class Solution:
    def climbStairs(self, n: int) -> int:

        # if staircases are less than 2
        # count of the ways to step up is same with n
        if n <= 2:
            return n

        # define array to memorize previous steps
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # use previous 2 cases(reach with 1 step and 2 step)
        # to find whole ways to reach current staircase
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        # return distinct ways to reach last staircase
        return dp[n]