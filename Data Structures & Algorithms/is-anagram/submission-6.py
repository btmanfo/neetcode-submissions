class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        premierTableau ={}
        deuxiemeTableau ={}


        for n in s:
            if n in premierTableau:
                premierTableau[n] = premierTableau[n]+1
            else:
                premierTableau[n] =1

        for i in t:
            if i in deuxiemeTableau:
                deuxiemeTableau[i]+=1
            else:
                deuxiemeTableau[i] =1
        
        return deuxiemeTableau ==  premierTableau