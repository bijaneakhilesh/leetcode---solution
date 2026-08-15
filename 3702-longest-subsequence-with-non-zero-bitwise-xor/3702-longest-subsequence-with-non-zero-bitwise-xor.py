class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for num in nums:
            ans ^=num
        if ans != 0:
            return n
        for num in nums:
            if num != 0:
                return n - 1
        return 0