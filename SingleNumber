//Finds the only number that isn't repeated twice in array

class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i += 2){
            if(i + 1 >= nums.length) return nums[i];
            if(nums[i] != nums[i + 1]) return nums[i];
        }
    //No repeats
    return -1;
    }
}
