class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,v in enumerate(nums):
            if i>0 and v == nums[i-1]:
                continue
            
            leftPtr = i+1
            rightPtr = len(nums) -1

            while leftPtr< rightPtr:
                threeSum = v + nums[leftPtr] + nums[rightPtr]

                if threeSum > 0:
                    rightPtr -=1
                elif threeSum < 0:
                    leftPtr +=1
                else:
                    res.append([v, nums[leftPtr], nums[rightPtr]])
                    leftPtr +=1
                    while nums[leftPtr] == nums[leftPtr -1] and leftPtr <rightPtr:
                        leftPtr +=1
        return res