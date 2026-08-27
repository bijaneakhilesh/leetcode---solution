class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        total = (sumB - sumA) // 2
        setB = set(bobSizes)
        for x in aliceSizes:
            if x + total in setB:
                return [x, x + total]