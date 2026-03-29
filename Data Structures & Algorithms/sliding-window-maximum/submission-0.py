class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output =[]
        q = collections.deque()
        l=r=0

        while(r<len(nums)):

            #Donc ici quand je vais te rajouter un nouvelle element, va verifier si le sommet est plus grand si il nest pas plus grans 
            #on va devoir le retirer au completA
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            #ca a pour but de faire en sorte que si cest un ancien items qui nest pas supposer etre dans notre nouveau window on va lenlever
            if l>q[0]:
                q.popleft()
            
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        
        return output