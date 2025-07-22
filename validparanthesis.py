class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map:  # It's a closing bracket
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        return not stack  # Valid if stack is empty