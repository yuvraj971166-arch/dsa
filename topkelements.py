class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # Count frequency (your logic)
        for i in range(len(nums)):
            count = 1
            num = nums[i]
            if num in freq:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            freq[num] = count
        
        # Sort by frequency
        sortedd = sorted(freq.items(), key=lambda x: x[1])
        top = sortedd[-k:]
        result = [i[0] for i in top]
        return result
