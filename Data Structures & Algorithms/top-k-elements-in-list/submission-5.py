class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listDesElements ={}
        freq =[]
        for i in range(len(nums)+1):
            freq.append([])
        
        for num in nums:
            if num in listDesElements:
                listDesElements[num] +=1
            else:
                listDesElements[num] = 1
        
        for n,j in listDesElements.items():
            freq[j].append(n)
        
        res =[]

        for i in range(len(freq)-1, 0, -1):
            for nums in freq[i]:
                res.append(nums)
                if len(res) == k:
                    return res
