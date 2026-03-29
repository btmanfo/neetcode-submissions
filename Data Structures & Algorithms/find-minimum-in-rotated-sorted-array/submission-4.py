class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        leftPtr = 0
        rightPtr = len(nums)-1

        while rightPtr >= leftPtr:
            #on fait ca pcq on sais que notre array est deja sorted, donc 
            #on a juste besoin de prend la valeur dans le leftPtr
            if nums[leftPtr] < nums[rightPtr]:
                res = min(res, nums[leftPtr])
                break

            middlePtr = leftPtr +(rightPtr - leftPtr)//2

            res = min(res, nums[middlePtr])

            #on doit faire un >= car mon middle ptr peut etre aussi le leftPtr. Ex: [2,1]
            if(nums[middlePtr]>= nums[leftPtr]):
                leftPtr = middlePtr +1
            else:
                rightPtr = middlePtr -1
        return res