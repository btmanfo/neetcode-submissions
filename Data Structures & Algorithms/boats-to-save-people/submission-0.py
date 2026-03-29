class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leftPtr = 0
        rightPtr = len(people)-1
        boat = 0
        while rightPtr >= leftPtr:
            if people[rightPtr] + people[leftPtr] <= limit:
                leftPtr += 1
            rightPtr -=1
            boat += 1
        return boat