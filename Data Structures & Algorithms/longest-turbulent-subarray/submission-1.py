class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        maxSize = 0
        if len(arr) == 1:
            return 1

        for i in range(n):
            currentValue = arr[i]
            j = i +1
            currenSize = 1
            findBigger = True
            while j < n:
                if findBigger == True:
                    if arr[j] < currentValue:
                        currenSize = 1
                        j+=1
                        findBigger = True
                        continue
                    else:
                        currenSize +=1
                        maxSize = max(maxSize, currenSize)
                        currentValue = arr[j]
                        j+=1
                        findBigger = False
                        continue
                else:
                    if arr[j] > currentValue:
                        currenSize = 1
                        j+=1
                        findBigger = True
                        continue
                    else:
                        currenSize +=1
                        maxSize = max(maxSize, currenSize)
                        currentValue = arr[j]
                        j+=1
                        findBigger = True
                        continue
        return maxSize
