class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1) 
        dp[0] = 0 
        for i in range(n):
            for j in range(1,4):
                if i + j <= n: 
                    dp[i + j] = min(dp[i + j], dp[i] + costs[i  + j - 1] + j**2)
        return dp[n]  