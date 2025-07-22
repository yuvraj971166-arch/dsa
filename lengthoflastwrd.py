class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces and split the string
        words = s.strip().split()
        return len(words[-1]) if words else 0
