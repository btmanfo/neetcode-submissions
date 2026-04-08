# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        leftPtr = 1
        rightPtr = n
        while leftPtr <= rightPtr:
            middlePtr = leftPtr + math.floor((rightPtr-leftPtr)/2)
            possible = guess(middlePtr)
            if possible == 0:
                return middlePtr
            elif possible == 1:
                leftPtr = middlePtr + 1
            elif possible == -1:
                rightPtr = middlePtr -1
        return -1
                