class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nbrApeared = {}
        for num in nums:
            if num not in nbrApeared:
                nbrApeared[num] = 1
            else:
                nbrApeared[num] += 1
        value = None
        appearedValue = None
        for i,j in nbrApeared.items():
            if value == None and appearedValue == None:
                value = i
                appearedValue = j
                print(i)
                print(j)
                continue
            if appearedValue < j:
                print(i)
                print(j)
                print(value)
                print(appearedValue)
                value = i
                appearedValue = j
        return value