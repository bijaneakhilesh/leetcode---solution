class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        min1 = arrays[0][0]
        max1 = arrays[0][-1]
        ans = 0
        for i in range(1, len(arrays)):
            min2 = arrays[i][0]
            max2 = arrays[i][-1]
            ans = max(ans, max(max1 - min2, max2 - min1))
            min1 = min(min1, min2)
            max1 = max(max1, max2)
        return ans