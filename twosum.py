class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # This will store {number: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # Found the pair
            num_map[num] = i  # Store the current number with its index
