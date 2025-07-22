from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start adding from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # If digit is 9, set to 0 and continue to carry over
        
        # If all digits were 9 (like 999), we need to add 1 at the start
        return [1] + digits
