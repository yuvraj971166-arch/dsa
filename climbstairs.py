class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n  # 1 way for step 1, 2 ways for step 2

        first, second = 1, 2  # Ways to reach step 1 and 2
        for _ in range(3, n + 1):
            first, second = second, first + second  # Fibonacci relation

        return second
