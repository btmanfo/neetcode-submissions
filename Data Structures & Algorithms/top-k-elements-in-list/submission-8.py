class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 i make a dictionnary with key as num and value as frequency
        # O(n) time complexty and O(n) space complexity
        elementFreq = {}
        for i in nums:
            if i not in elementFreq:
                elementFreq[i] = 1
            else:
                elementFreq[i]+=1
        print(elementFreq)

        #2 make a table of tuple with tuple[0] num and tuple[1] frequency
        # O(n) time complexiyy and O(n) space complexity
        arrayTuple = []
        for i,j in elementFreq.items():
            arrayTuple.append((i,j))
        
        #3 Sort the array base on tuple[1]
        # O(nlogn) time complexity
        arrayTuple.sort(key = lambda x:x[1], reverse = True)

        #4 return value
        value = []
        for i in range(k):
            value.append(arrayTuple[i][0])
        return value