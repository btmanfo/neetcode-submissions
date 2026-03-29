class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        listSet = set(nums)
        longest = 0

        for num in listSet:
            if num - 1 not in listSet:
                current_num = num
                current_streak = 1

                while current_num + 1 in listSet:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest