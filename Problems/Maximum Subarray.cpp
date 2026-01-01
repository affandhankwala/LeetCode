//Finds the largest sum of integers that are contigious in an array

class Solution {
    public int maxSubArray(int[] nums) {
        //We will define the maximum summation
        int max = nums[0]; 
        //Set to initial number to compensate for 'at least one number' restriction
        //Set current sum to nums[0]
        int sum = nums[0];
        
        //Loop through entire array
        for(int i = 1; i < nums.length; i++){
            //Keep adding to sum until sum is negative
            //If negative then we move to next number
            if(sum < 0) sum = nums[i];
            else{
                sum += nums[i];
            }
            //Compare current sum with max and adjust if max is smaller
            max = Math.max(max,sum);
        }
        return max;
    }
}
