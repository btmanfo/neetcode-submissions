class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n= len(gas)

        for i in range(n):
            tank = gas[i] - cost[i]
            if tank < 0:
                continue
            j = (i+1)%n

            while i != j:
                tank += gas[j]
                tank -= cost[j]

                if tank< 0:
                    break
                
                j = (j+1)%n
            if i == j:
                return i
        return -1