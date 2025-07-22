class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # sqrt(0) = 0, sqrt(1) = 1

        left, right = 1, x // 2  # sqrt(x) is always <= x/2 for x > 1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # When loop ends, right is the floor of sqrt(x)
