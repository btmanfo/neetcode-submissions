class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nums = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in nums:
                nums[sorted_word] = []
            nums[sorted_word].append(word)
        return list(nums.values())
