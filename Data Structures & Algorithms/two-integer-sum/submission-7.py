class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr =[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]+nums[j] == target):
                    if(i!=j):
                        if(len(arr)==0):
                            arr.append(i)
                            arr.append(j)
        return arr;
                    
        