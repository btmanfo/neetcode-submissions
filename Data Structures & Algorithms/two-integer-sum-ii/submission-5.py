class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers = [1,2,3,4]  target = 3
        listOfNumber = {}

        for i in range(len(numbers)):
            listOfNumber[numbers[i]] = i
        
        #listOfNumbers = {1:0, 2:1, 3:2, 4:3}
        for i in range(len(numbers)):
            newTarget = target - numbers[i]

            if newTarget in listOfNumber and i != listOfNumber[newTarget]:
                return [i+1, listOfNumber[newTarget]+1]
        return [0,0]