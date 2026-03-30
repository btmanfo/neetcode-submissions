class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #1 sort arr
        nums.sort()
        #2 array without negative number
        sortedPos = []
        for num in nums:
            if num >= 0:
                sortedPos.append(num)
        setValues = set()
        for num in sortedPos:
            setValues.add(num)
        for i in range(sortedPos[0], sortedPos[-1]+2):
            if i not in setValues:
                return i
        return None

