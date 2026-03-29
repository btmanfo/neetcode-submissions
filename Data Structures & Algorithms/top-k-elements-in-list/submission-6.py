class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyApearence = []
        #on doit mettre +1 car lelement a lindex 0 est quand elle est vide
        for i in range(len(nums)+1):
            frequencyApearence.append([])
        
        numberOfAppearance = {}
        for i in nums:
            numberOfAppearance[i] = 1 + numberOfAppearance.get(i, 0)
        
        for i,j in numberOfAppearance.items():
            frequencyApearence[j].append(i)
        
        res = []
        w =k
        #on pourrait mettre quil nexecute pas celui a lindex 0
        for i in range(len(frequencyApearence)-1, -1,-1):
            for j in frequencyApearence[i]:
                res.append(j)
                w = w-1
                if(w ==0):
                    return res
                

