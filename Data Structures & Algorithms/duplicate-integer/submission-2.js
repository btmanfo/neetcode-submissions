class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let number = false
        for(let n in nums){
            for(let j in nums){
                if(nums[n] == nums[j] && n != j){
                    number = true
                }
            }
        }
        return number
    }
}
