class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        result = []

        for word in strs:
            key = ''.join(sorted(word))  # Sort letters to form a key
            if key in groups:
                index = groups.index(key)
                result[index].append(word)
            else:
                groups.append(key)
                result.append([word])

        return result
