class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length){
            return false
        }

        let mot1 = s.split('').sort().join('')
        let mot2 = t.split('').sort().join('')
        if (mot1 == mot2){
            return true
        }
        else{
            return false
        }
    }
}
