class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total %4 != 0:
            return False
        sample = [0,0,0,0]
        matchsticks.sort(reverse=True)
        def backprapagation(i):
            if i == len(matchsticks):
                return sample[0] == sample[1] == sample[2] == sample[3]
            for side in range(4):
                if sample[side] + matchsticks[i] <= total:
                    sample[side] += matchsticks[i]

                    if backprapagation(i + 1):
                        return True
                    # we backtrack when the solution is not valid
                    sample[side] -= matchsticks[i]
            return False
        return backprapagation(0)
