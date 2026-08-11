class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen = set(nums)
        count = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count += nums[i + 1]
            else:
                break
        while count in seen:
            count += 1
        return count
