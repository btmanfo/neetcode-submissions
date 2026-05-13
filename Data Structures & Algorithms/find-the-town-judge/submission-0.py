class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # define all people with bool to see if they are trusting someone
        people = [True]*n

        # (trustRelation[0]-1) represent someone that is trusting so he doesnt qualify ad judge
        for trustRelation in trust:
            people[trustRelation[0]-1] = False
        
        # we loop to all the people to find the one that doent trust someone
        for i in range(len(people)):
            if people[i] == False:
                continue
            newPeople = [True]*n
            newPeople[i] = False
            for trustRelation in trust:
                if trustRelation[1] == i+1:
                    newPeople[trustRelation[0]-1] = False
            isValid = True
            for j in newPeople:
                if j == True:
                    isValid = False
            if isValid:
                return i+1
        return -1

             