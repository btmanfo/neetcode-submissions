class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) -1
        while leftPtr< rightPtr:
            res = numbers[leftPtr] + numbers[rightPtr]
            if res>target:
                rightPtr -=1
            elif res<target:
                leftPtr +=1
            else:
                return [leftPtr+1, rightPtr+1]
        return [-1,-1]