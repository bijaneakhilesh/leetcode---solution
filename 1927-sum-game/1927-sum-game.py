class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left = num[:half]
        right = num[half:]
        left_q = left.count('?')
        right_q = right.count('?')
        left_sum = sum(int(c) for c in left if c != '?')
        right_sum = sum(int(c) for c in right if c != '?')
        if (left_q + right_q) % 2 == 1:
            return True
        return left_sum - right_sum != 9 * (right_q - left_q) // 2 