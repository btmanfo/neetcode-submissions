class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        allCombination = set()
        def backpropagation(arr):
            if len(arr) == 4:
                allCombination.add(tuple(arr.copy()))
                return
            for i in range(len(matchsticks)):
                if matchsticks[i] != float('-inf'):
                    arr.append(matchsticks[i])
                    matchsticks[i] = float('-inf')
                    backpropagation(arr)
                    matchsticks[i] = arr[-1]
                    arr.pop()
        backpropagation([])
        allCombination = list(allCombination)
        for subset in allCombination:
            newSub = sorted(list(subset))
            if newSub[0] == newSub[1] and newSub[2] == newSub[3]:
                return True
        return False
