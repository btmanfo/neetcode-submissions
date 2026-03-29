class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="": return ""

        countT, window ={},{}
        for c in t:
            countT[c] = 1+ countT.get(c,0) #on utilise get comme ca si il est pas la on lui donne une valeur de 0

        have, need =0, len(countT)
        
        res = [-1,-1] #Donc ici on a la index de notre element plus petit
        resLen = float("infinity") #donc on a notre nombre le plus petit qui va etre au commencement infini
        l =0
        for r in range(len(s)):
            c = s[r]

            window[c] = 1+ window.get(c,0)  #donc la je te rajoute la valeur dans notre window

            #donc la je te regarde si la valeur est dans notre conntT et que la valeur de notre window a c et la meme que celle dans count 
            if c in countT  and window[c] == countT[c]:
                have+=1     #donc si cest le cas on va augmenter la valeur de 1

            
            while have == need:     #donc on va loop jusqua que ca soit egal
                if(r- l+1) < resLen:     #donc on va regarder si la taille nouvelle est plus petit que lancien
                    res =[l,r]
                    resLen = r-l+1

                #donc la faut reduire notre au left ainsi on decide denlever celui a notre left dans notre window
                window[s[l]] -=1

                #mais la on doit update notre "have" donc si cetait un element quon chuiche et quil devient
                #plus petit il faut reduire notre have
                if s[l] in countT and window[s[l]]< countT[s[l]]:
                    have -= 1       #donc la on va le reduire ce qui va nous faire sortir de la loop
                
                l+=1
            
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""                          